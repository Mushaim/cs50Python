import requests
import sys

def main():
    try:
        if len(sys.argv) == 2:
            if float(sys.argv[1]):
                amount = calculate_total(float(sys.argv[1]))
                print(f"${amount:,.4f}")
            else:
                sys.exit("Only integer are allowed")
        else:
            sys.exit("Only 1 argument is allowed")
    except ValueError:
        sys.exit("wrong value")

def calculate_total(n):
    price = get_price()
    return price*n

def get_price():
    try:
        r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=6c5895aec8cadecd3295585f8eea7126387bec82337111adbc4a6bfad363c354")
        readable = r.json()
        data =  readable["data"]
        return float(data["priceUsd"])
    except requests.RequestException:
        sys.exit("Bad request")
main()
