#!/usr/bin/python3
import pika
import sys
import time
import psutil
import json
import socket
import settings

time.sleep(20)

SLEEP_TIME = 0.5  # seconds

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=settings.RABBITMQ_HOST))
channel = connection.channel()

channel.exchange_declare(exchange=settings.RABBITMQ_EXCHANGE,
                         exchange_type=settings.RABBITMQ_EXCHANGE_TYPE)

routing_key = '{}.measure'.format(socket.gethostname(),)


while True:
    try:
        cpu_percentage = psutil.cpu_percent(interval=1)
        message = {'cpu_percentage': cpu_percentage}
        channel.basic_publish(exchange=settings.RABBITMQ_EXCHANGE,
                      routing_key=routing_key,
                      body=json.dumps(message))
    finally:
        time.sleep(SLEEP_TIME)
