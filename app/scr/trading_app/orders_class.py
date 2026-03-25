from datetime import datetime
import random

class Order:

    def __init__(self, username: str, side: str, quantity: int, price: float):


        self.order_id  = f"{random.randint(11, 9999)}"
        self.username  = username
        self.side      = side.upper()
        self.quantity  = quantity
        self.price     = price
        self.stock     = "XYZ Corp"
        self.timestamp = datetime.now()

    def to_dict(self) -> dict:

        return {
            "order_id"  : self.order_id,
            "username"  : self.username,
            "side"      : self.side,
            "quantity"  : self.quantity,
            "price"     : self.price,
            "stock"     : self.stock,
            "timestamp" : self.timestamp.isoformat()
        }
        