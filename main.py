import requests

class YoBitAPI:
    def __init__(self):
        self.base_url = "https://yobit.net/api/3"

    def save_to_file(self, file_name, content):
        with open(file_name, "w") as file:
            file.write(content)

    def get_info(self):
        response = requests.get(f"{self.base_url}/info")
        self.save_to_file("results/info.txt", response.text)
        return response.text

    def get_ticker(self, coin1="btc", coin2="usd"):
        response = requests.get(f"{self.base_url}/ticker/{coin1}_{coin2}?ignore_invalid=1")
        self.save_to_file("results/ticker.txt", response.text)
        return response.text

    def get_depth(self, coin1="btc", coin2="usd", limit=150):
        response = requests.get(f"{self.base_url}/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")
        self.save_to_file("results/depth.txt", response.text)
        bids = response.json()[f"{coin1}_{coin2}"]["bids"]
        total_bids_amount = sum(price * coin_amount for price, coin_amount in bids)
        return f"Total bids: {total_bids_amount} $"

    def get_trades(self, coin1="btc", coin2="usd", limit=150):
        response = requests.get(f"{self.base_url}/trades/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")
        self.save_to_file("results/trades.txt", response.text)
        trades = response.json()[f"{coin1}_{coin2}"]
        total_trade_ask = sum(item["price"] * item["amount"] for item in trades if item["type"] == "ask")
        total_trade_bid = sum(item["price"] * item["amount"] for item in trades if item["type"] == "bid")
        return f"[-] TOTAL {coin1} SELL: {round(total_trade_ask, 2)} $, [+] TOTAL {coin1} BUY: {round(total_trade_bid, 2)} $"

def main():
    yobit = YoBitAPI()
    print(yobit.get_info())
    print(yobit.get_ticker())
    print(yobit.get_ticker(coin1="eth"))
    print(yobit.get_depth())
    print(yobit.get_depth(coin1="doge"))
    print(yobit.get_depth(coin1="doge", limit=2000))
    print(yobit.get_trades())
    print(yobit.get_trades(coin1="xrp"))
    print(yobit.get_trades(coin1="doge"))


if __name__ == '__main__':
    main()