import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_API_SECRET"),
            testnet=True
        )
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def create_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)
