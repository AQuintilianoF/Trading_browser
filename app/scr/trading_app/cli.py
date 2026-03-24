import os
from trading_app.order_service import send_order
from trading_app.config        import RabbitConfig

STOCK    = "XYZ Corp"
QUANTITY = 100

def main():

    print("\n" + "=" * 40)
    print("       Welcome to Trading App")
    print(f"       Stock: {STOCK}")
    print("=" * 40)
    print(""" Enter your preference
    1 - Buy  stocks
    2 - Sell stocks
    0 - Exit
    """)

    while True:
        try:
            index = int(input(" > "))
            if index in (0, 1, 2):
                break
            print(" Value is not in index")

        except ValueError:
            print("[Error] Please enter a valid number")

    match index:
        case 1:
            vender("BUY")
        case 2:
            vender("SELL")
        case 0:
            print("Exiting...")
            os.system("exit")

def vender(side):

    print("\n" + "=" * 40)
    print(f"  {side} ORDER — {STOCK}")
    print(f"  Quantity : {QUANTITY} shares")
    print("=" * 40)

    username = input("Username             : ")
    
    price    = float(input("Price per share ($)  : "))

    config = RabbitConfig()
    msg = send_order(username, side , QUANTITY, price, config)
    print(msg)


    input("\nPress Enter to return to menu...")
    main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[system] Leaving system...")