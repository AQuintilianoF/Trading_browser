from trading_app.orders_class import Order
from trading_app.trade_class  import Trade

class OrderBook:

    def __init__(self):
        self.buys  : list[Order] = []
        self.sells : list[Order] = []

    def match(self, incoming: Order) -> Trade | None:

        if incoming.side == "BUY":
            candidates = [i for i in self.sells if i.price <= incoming.price]
            if not candidates:
                self.buys.append(incoming)
                return None
            # pega o vendedor com menor preço
            best  = min(candidates, key=lambda x: x.price)
            trade = Trade(best, incoming, best.price)
            self.sells.remove(best)
            return trade

        elif incoming.side == "SELL":
            candidates = [o for o in self.buys if o.price >= incoming.price]
            if not candidates:
                self.sells.append(incoming)
                return None
            # pega o comprador com maior preço
            best  = max(candidates, key=lambda o: o.price)
            trade = Trade(incoming, best, best.price)
            self.buys.remove(best)
            return trade

    def display(self):
        print("\n--- ORDER BOOK ---")
        print(f"  BUYS  ({len(self.buys)})  : {[f'${o.price} by {o.username}' for o in self.buys]}") (f"  SELLS ({len(self.sells)}) : {[f'${o.price} by {o.username}' for o in self.sells]}")
        
        print("------------------\n")