from trading_app.orders_class import Order
from trading_app.trade_class  import Trade
from itertools import zip_longest

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
        print ("BUYS".ljust(40) + "| SELLS") 
        print("ID".ljust(10)+ "| NOME".ljust(15)+"| PRICE".ljust(15)+ "| ID".ljust(10)+ "| NOME".ljust(15)+ "| PRICE".ljust(15))


        for buy_side , sell_side in zip_longest (self.buys, self.sells):

            buy_str = ''
            sell_str = ''

            if buy_side:
                buy_str = f"{buy_side.order_id[0]}".ljust(10) + f"| {buy_side.username}".ljust(15)+ f"| ${buy_side.price:.2f}".ljust(15)

            if sell_side:
                sell_str = f"| {sell_side.order_id[0]}".ljust(10)+ f"| {sell_side.username}".ljust(15)+ f"| ${sell_side.price:.2f}".ljust(15)

        print (f"{buy_str}".ljust(40) + f"{sell_str}".ljust(20))
        print("-" * (40 * 2 + 3))
        print(f"Total Buys: {len(self.buys)} | Total Sells: {len(self.sells)}")
        print("-" * (40 * 2 + 3))