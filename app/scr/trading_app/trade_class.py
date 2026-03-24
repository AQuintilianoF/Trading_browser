from datetime import datetime
import uuid

class Trade:

    def __init__(self, buy_order, sell_order, price: float):

        self.trade_id  = str(uuid.uuid4())
        self.buyer     = buy_order.username
        self.seller    = sell_order.username
        self.quantity  = buy_order.quantity
        self.price     = price
        self.stock     = "XYZ Corp"
        self.timestamp = datetime.now()

    def to_dict(self) -> dict:

        return {
            "trade_id"  : self.trade_id,
            "buyer"     : self.buyer,
            "seller"    : self.seller,
            "quantity"  : self.quantity,
            "price"     : self.price,
            "stock"     : self.stock,
            "timestamp" : self.timestamp.isoformat()
        }