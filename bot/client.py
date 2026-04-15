from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    client = Client(
        api_key=os.getenv("API_KEY"),
        api_secret=os.getenv("API_SECRET")
    )
    
    # Set Testnet
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    
    return client