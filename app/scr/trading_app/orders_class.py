from datetime import datetime
import uuid

class Order:

    def __init__(self, username: str, side: str, quantity: int, price: float):

        self.order_id  = str(uuid.uuid4())
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
        