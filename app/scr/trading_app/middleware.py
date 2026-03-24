import pika
from trading_app.config import RabbitConfig

def create_connection(config: RabbitConfig = None):

    if config is None:
        config = RabbitConfig()

    parameters = pika.URLParameters(config.url)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    
    # Exchange para ordens enviadas pelos traders
    channel.exchange_declare(
        exchange      = "orders",
        exchange_type = "direct",
        durable       = True
    )

    # Exchange para trades executados pelo matching engine
    channel.exchange_declare(
        exchange      = "trades",
        exchange_type = "fanout",
        durable       = True
    )

    return connection, channel