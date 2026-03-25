from trading_app.orders_class import Order
from trading_app.trade_class  import Trade
from itertools import zip_longest
import os

class OrderBook:

    def __init__(self):
        self.buys  : list[Order] = []
        self.sells : list[Order] = []

    def match(self, new_order: Order) -> Trade | None:

        candidates_orders = []
        os.system("cls")
        if new_order.side == "BUY":
            
            for x in self.sells:
                if x.price <= new_order.price:
                    candidates_orders.append(x)

            if not candidates_orders:
                self.buys.append(new_order)
                return None
            
            best  = min(candidates_orders, key=lambda x: x.price)
            trade = Trade( new_order, best, best.price)
            self.sells.remove(best)
            return trade

        elif new_order.side == "SELL":
            
            for x in self.buys:
                if x.price >= new_order.price:
                    candidates_orders.append(x)

            if not candidates_orders:
                self.sells.append(new_order)
                return None
            
            best  = max(candidates_orders, key=lambda x: x.price)
            trade = Trade(best, new_order,  best.price)
            self.buys.remove(best)
            return trade

    def display(self):
        print("\n--- ORDER BOOK ---")
        print ("BUYS".ljust(40) + "| SELLS") 
        print("ID".ljust(10)+ "| NOME".ljust(15)+"| PRICE".ljust(15)+ "| ID".ljust(10)+ "| NOME".ljust(15)+ "| PRICE".ljust(15))

        self.buys.sort(reverse=True, key=lambda x: x.price)
        self.sells.sort(key=lambda x: x.price)

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