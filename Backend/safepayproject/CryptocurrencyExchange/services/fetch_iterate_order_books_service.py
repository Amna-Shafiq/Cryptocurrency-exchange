import requests
from django.conf import settings

BINANCE_URL = 'https://api.binance.com/api/v3/depth?symbol=BTCUSDT'
COINBASE_URL = 'https://api-public.sandbox.exchange.coinbase.com/products/BTC-USD/book?level=3'
BITFINEX_URL = 'https://api.bitfinex.com/v1/book/btcusd'

class ExchangeAPIService:
    @staticmethod
    def get_exchange_data(url):
        try:
            return requests.get(url).json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f'Error fetching data from API: {str(e)}')

    def get_binance_data(self):
        return self.get_exchange_data(BINANCE_URL)

    def get_coinbase_data(self):
        return self.get_exchange_data(COINBASE_URL)

    def get_bitfinex_data(self):
        return self.get_exchange_data(BITFINEX_URL)

    def find_lowest_price_binance(self,asks_data, target_amount):
        lowest_price = None

        for ask_price, ask_amount in asks_data:
            ask_price = float(ask_price)
            ask_amount = float(ask_amount)

            if ask_amount >= target_amount:
                if lowest_price is None or ask_price < lowest_price:
                    lowest_price = ask_price

        return lowest_price

    def find_lowest_price_coinbase(self,asks_data, target_amount):
        lowest_price = None

        for ask_price, ask_amount, _ in asks_data:
            ask_price = float(ask_price)
            ask_amount = float(ask_amount)

            if ask_amount >= target_amount:
                if lowest_price is None or ask_price < lowest_price:
                    lowest_price = ask_price

        return lowest_price

    def find_lowest_price_bitfinex(self, asks_data, target_amount):
        lowest_price = None

        for ask in asks_data:
            ask_price = float(ask.get("price", 0))
            ask_amount = float(ask.get("amount", 0))

            if ask_amount >= target_amount:
                if lowest_price is None or ask_price < lowest_price:
                    lowest_price = ask_price

        return lowest_price


