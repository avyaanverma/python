import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

#
while True:
    try:
        jsnfile = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.RequestException:
        continue
    else:
        break

# jsnfile = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

# 'Response' object is not subscriptable
# This means convert to json first


# json function changes into a string and json.dumps() formats in json type


# print(json.dumps(jsnfile.json(), indent=2))

# {
#   "time": {
#     "updated": "Jul 6, 2023 09:10:00 UTC",
#     "updatedISO": "2023-07-06T09:10:00+00:00",
#     "updateduk": "Jul 6, 2023 at 10:10 BST"
#   },
#   "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
#   "chartName": "Bitcoin",
#   "bpi": {
#     "USD": {
#       "code": "USD",
#       "symbol": "&#36;",
#       "rate": "31,377.3173",
#       "description": "United States Dollar",
#       "rate_float": 31377.3173
#     },
#     "GBP": {
#       "code": "GBP",
#       "symbol": "&pound;",
#       "rate": "26,218.6353",
#       "description": "British Pound Sterling",
#       "rate_float": 26218.6353
#     },
#     "EUR": {
#       "code": "EUR",
#       "symbol": "&euro;",
#       "rate": "30,566.0881",
#       "description": "Euro",
#       "rate_float": 30566.0881
#     }
#   }
# }

# print(type(dict(jsnfile)))
conversion_price_bitcoin = jsnfile["bpi"]["USD"]["rate"]
conversion_price = ""
for no in conversion_price_bitcoin:
    if no.isdigit() or no == '.': conversion_price += no

conversion_price = float(conversion_price)



amount = float(sys.argv[1])
print(f"${amount*conversion_price:,}")