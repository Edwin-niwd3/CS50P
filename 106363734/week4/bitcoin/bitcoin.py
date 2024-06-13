import sys
import requests

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        bitcoin_amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    bitcoin_info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_json = bitcoin_info.json()
    bitcoin_rate = float(bitcoin_json["bpi"]["USD"]["rate_float"])
    price = bitcoin_rate * bitcoin_amount
    print(f"${price:,.4f}")
except requests.RequestException:
    print("ERROR")
