import argparse
from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        side = validate_side(args.side.upper())
        order_type = validate_order_type(args.type.upper())
        quantity = validate_quantity(args.quantity)

        if order_type == "LIMIT" and not args.price:
            raise ValueError("LIMIT order requires --price")

        client = BinanceFuturesClient()

        response = place_order(
            client,
            symbol=args.symbol.upper(),
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=args.price
        )

        print("\n===== ORDER SUCCESS =====")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")

if __name__ == "__main__":
    main()
