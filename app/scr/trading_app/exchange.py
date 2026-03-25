import pika
from trading_app.middleware   import create_connection
from trading_app.orders_class import Order
from trading_app.pers_json   import serialize, deserialize
from trading_app.order_book   import OrderBook

QUEUE = "orders.queue"

def main():

    connection, channel = create_connection()
    book                = OrderBook()

    
    channel.queue_declare(queue=QUEUE, durable=True)
    channel.queue_bind(
        queue       = QUEUE,
        exchange    = "orders",
        routing_key = "BUY"
    )
    channel.queue_bind(
        queue       = QUEUE,
        exchange    = "orders",
        routing_key = "SELL"
    )

    print("[Exchange] Waiting for orders. CTRL+C to stop.\n")

    def on_order(ch, method, properties, body):

        data  = deserialize(body)
        order = Order(
            username = data["username"],
            side     = data["side"],
            quantity = data["quantity"],
            price    = data["price"]
        )

        print(f"[Received] {order.side} {order.quantity} shares at ${order.price:.2f} from {order.username}")

        trade = book.match(order)

        if trade:
            print(f"\n\n[Match!]   Trade executed at ${trade.price:.2f} — {trade.buyer} bought from {trade.seller}")
            ch.basic_publish(
                exchange    = "trades",
                routing_key = "",
                body        = serialize(trade),
                properties  = pika.BasicProperties(delivery_mode=2)
            )
        else:
            print(f"[No match] Order added to book")

        book.display()
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=QUEUE, on_message_callback=on_order)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\n[Exchange] Shutting down...")
        connection.close()

if __name__ == "__main__":
    main()