#!/usr/bin/python3
import pika
import json
import settings
import time

time.sleep(20)


connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_HOST))
channel = connection.channel()
channel.exchange_declare(exchange=settings.RABBITMQ_EXCHANGE,
                             exchange_type=settings.RABBITMQ_EXCHANGE_TYPE)

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange=settings.RABBITMQ_EXCHANGE,
                           queue=queue_name,
                           routing_key=settings.RABBITMQ_SUB)

def callback(ch, method, properties, body):
    machine = method.routing_key.split(".")[0]
    result = analyze(json.loads(body.decode('utf-8'))['cpu_percentage'])
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=settings.RABBITMQ_HOST))
    channel = connection.channel()
    channel.exchange_declare(exchange=settings.RABBITMQ_EXCHANGE,
                         exchange_type=settings.RABBITMQ_EXCHANGE_TYPE)
    routing_key = settings.RABBITMQ_PUB.format(machine)
    channel.basic_publish(exchange=settings.RABBITMQ_EXCHANGE,
                      routing_key=routing_key,
                      body=json.dumps({'cpu_result': result}))
    connection.close()

    
def analyze(percentage):
    if percentage < 25:
        result = 'LOW'
    elif percentage < 75:
        result = 'MEDIUM'
    else:
        result = 'HIGH'
    return result

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()


