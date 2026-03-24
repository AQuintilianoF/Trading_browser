 **It allows commands to be given via the VS terminal.**
 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
 
# Trading App

The system consists of:
- **`cli.py`**: A command-line client for traders to send buy (BUY) or sell (SELL) orders.
- **`exchange.py`**: The central server that acts as the "matching engine". It receives orders, attempts to match them, and if a match occurs, executes a trade.

## Prerequisites

Before running the project, you will need to have the following installed:

 **Python 3.8+**: Download and install the latest version of Python.

2.  **Create a virtual environment:**
    python -m venv .venv

3.  **Activate the virtual environment:**
    *   **Windows:**  
    .venv\Scripts\activate
       
4.  **Install dependencies:**
    pip install -r requirements.txt

5.  **Create the `.env` file:**
    In the project root, create a file named `.env` and add the following line:
    
    AMQP_URL="amqp://guest:guest@localhost:5672/%2F"(I sent you that part on WhatsApp.)

## How to Run

*at least two terminals*

1.  **Terminal 1: Start the Exchange (Matching Engine)**
    This terminal will run the server that processes orders.
    cd app
    cd scr
    python -m trading_app.exchange
    You will see the message `[Exchange] Waiting for orders. CTRL+C to stop.`

2.  **Terminal 2 (and others): Send Orders with the CLI Client**
    Open a new terminal (or more, to simulate multiple traders) and run the client.
    cd app
    cd scr
    python -m trading_app.cli
    
    Follow the on-screen instructions to send buy or sell orders.


