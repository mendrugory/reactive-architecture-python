#!/usr/bin/python3
import os
import pika
import json
from tornado import web, websocket, ioloop
import settings
import logging
import uuid


class RabbitMQ:
    def __init__(self, func):
        self.connection, self.channel = None, None
        self.connecting = False
        self.connected = False
        self.channel = None
        self.connection = None
        self.func = func
        self.queue_name = "{}__{}".format(settings.RABBITMQ_QUEUE, uuid.uuid4())

    def connect(self):
        if self.connecting:
            return
        self.connecting = True
        param = pika.ConnectionParameters(host=settings.RABBITMQ_HOST)
        self.connection = pika.adapters.tornado_connection.TornadoConnection(
            param,
            on_open_callback=self.on_connected,
            on_open_error_callback=self.on_connection_error,
            on_close_callback=self.close)

    def add_on_connection_close_callback(self):
        """This method adds an on close callback that will be invoked by pika
        when RabbitMQ closes the connection to the publisher unexpectedly.

        """
        self.connection.add_on_close_callback(self.close)

    def on_connected(self, connection):
        self.connected = True
        self.connecting = False
        self.connection = connection
        self.add_on_connection_close_callback()
        self.connection.channel(self.on_channel_open)

    def on_connection_error(self, method, message):
        logging.error("Method: {}\n Message: {}".format(method, message))

    def on_channel_open(self, channel):
        self.channel = channel
        self.add_on_channel_close_callback()
        self.channel.exchange_declare(exchange=settings.RABBITMQ_EXCHANGE,
                                      exchange_type=settings.RABBITMQ_EXCHANGE_TYPE,
                                      callback=self.on_exchange_declared)

    def on_exchange_declared(self, frame):
        self.channel.queue_declare(auto_delete=True,
                                   queue=self.queue_name,
                                   durable=False,
                                   exclusive=True,
                                   callback=self.on_queue_declared)

    def on_queue_declared(self, frame):
        self.channel.queue_bind(exchange=settings.RABBITMQ_EXCHANGE,
                                queue=self.queue_name,
                                routing_key=settings.RABBITMQ_SUB,
                                callback=self.on_queue_bound)

    def on_queue_bound(self, frame):
        self.channel.basic_consume(consumer_callback=self.func,
                                   queue=self.queue_name,
                                   no_ack=True)

    def close(self):
        if self.channel and self.channel.is_open:
            self.channel.close()
        if self.connection and self.connection.is_open:
            self.connection.close()

    def add_on_channel_close_callback(self):
        self.channel.add_on_close_callback(self.on_channel_closed)

    def on_channel_closed(self, channel, reply_code, reply_text):
        self.connection.close()


class TornadoWebSocketHandler(websocket.WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rabbitmq_client = None

    def data_received(self, chunk):
        pass

    def check_origin(self, origin):
        return True

    def send_to_the_client(self, data):
        try:
            self.write_message(data)
        except websocket.WebSocketClosedError as e:
            self.on_close()

    def open(self):
        self.rabbitmq_client = RabbitMQ(self.callback)
        self.rabbitmq_client.websocket = self
        ioloop.IOLoop.current().add_timeout(100, self.rabbitmq_client.connect)

    def on_close(self):
        if self.rabbitmq_client:
            self.rabbitmq_client.close()

    def callback(self, channel, method, header, body):
        machine = method.routing_key.split(".")[0]
        data = json.loads(body.decode("utf-8"))
        data['machine'] = machine
        try:
            self.write_message(data)
        except websocket.WebSocketClosedError as e:
            self.on_close()

    def on_message(self, message):
        print(message)


class IndexHandler(web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render("index.html")


def make_app():
    tornado_settings = {
        "template_path": os.path.dirname(__file__),
        "static_path": os.path.dirname(__file__)
    }
    return web.Application([
        (r"/", IndexHandler),
        (r"/ws", TornadoWebSocketHandler),
    ], **tornado_settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    logging.info("http://localhost:8888")
    ioloop.IOLoop.current().start()
