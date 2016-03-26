import logging

# Logger
logging.basicConfig(filename='web.log',
                    format='%(asctime)s - %(name)s -  %(module)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

RABBITMQ_HOST = 'rabbitmq'
RABBITMQ_EXCHANGE = 'my_exchange'
RABBITMQ_EXCHANGE_TYPE = 'topic'
RABBITMQ_SUB = '*.analysis'
RABBITMQ_QUEUE = 'queue_web'
