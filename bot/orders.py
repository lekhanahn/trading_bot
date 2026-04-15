import logging
import random
from datetime import datetime

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"[MOCK] Placing order: {symbol} {side} {order_type} {quantity} {price}")

        # Fake response (simulate Binance)
        order = {
            "orderId": random.randint(10000, 99999),
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "status": "FILLED" if order_type == "MARKET" else "NEW",
            "executedQty": quantity if order_type == "MARKET" else "0",
            "avgPrice": price if price else "Market Price",
            "time": str(datetime.now())
        }

        logging.info(f"[MOCK RESPONSE]: {order}")
        return order

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise