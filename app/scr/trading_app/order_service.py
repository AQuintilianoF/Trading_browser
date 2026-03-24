import pika
from trading_app.middleware  import create_connection
from trading_app.orders_class import Order
from trading_app.pers_json  import serialize
from trading_app.config      import RabbitConfig

EXCHANGE = "orders"

def send_order(username: str, side: str, quantity: int, price: float, config: RabbitConfig = None):

    order              = Order(username, side, quantity, price)
    connection, channel = create_connection(config)

    try:
        channel.basic_publish(
            exchange    = EXCHANGE,
            routing_key = order.side,
            body        = serialize(order),
            properties  = pika.BasicProperties(delivery_mode=2)
        )
        return (f"[Congrats!!!] Order sent: {order.side} {order.quantity} shares of {order.stock} at ${order.price}")

    finally:
        connection.close()

        