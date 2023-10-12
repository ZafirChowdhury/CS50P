import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    coin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

bitcoin_info_json = (requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")).json()
bitcoin_price = float(bitcoin_info_json["bpi"]["USD"]["rate"].replace(",", ""))

price = "{:,.4f}".format((coin * bitcoin_price))

print(f"${price}")