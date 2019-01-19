import logging, sys

# Logger
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s'))
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

RABBITMQ_HOST = 'rabbitmq'
RABBITMQ_EXCHANGE = 'my_exchange'
RABBITMQ_EXCHANGE_TYPE = 'topic'
RABBITMQ_SUB = '*.analysis'
RABBITMQ_QUEUE = 'queue_web'
