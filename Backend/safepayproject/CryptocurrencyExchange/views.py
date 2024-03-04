from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view(['GET'])
def exchange_rate(request):
    try:
        amount = float(request.GET.get('amount', 0))
    except ValueError:
        return Response({'error': 'Invalid amount provided'}, status=400)

    if amount <= 0:
        return Response({'error': 'Amount must be greater than zero'}, status=400)

    binance_url = 'https://api.binance.com/api/v3/depth?symbol=BTCUSDT'
    coinbase_url = 'https://api-public.sandbox.exchange.coinbase.com/products/BTC-USD/book?level=3'

    try:
        binance_data = requests.get(binance_url).json()
        coinbase_data = requests.get(coinbase_url).json()
    except requests.exceptions.RequestException as e:
        return Response({'error': f'Error fetching data from external APIs: {str(e)}'}, status=500)

    binance_data_asks = binance_data.get("asks", [])
    coinbase_data_asks = coinbase_data.get("asks", [])

    binance_price = find_lowest_price_binance(binance_data_asks, amount)
    coinbase_price = find_lowest_price_coinbase(coinbase_data_asks, amount)
    
    if binance_price is not None and (coinbase_price is None or binance_price < coinbase_price):
        best_price = binance_price
    elif coinbase_price is not None:
        best_price = coinbase_price
    else:
        best_price = None
        
    response_data = {
        'binance_price': binance_price,
        'coinbase_price': coinbase_price,
        'best_price': best_price
    }

    return Response(response_data)

def find_lowest_price_binance(asks_data, target_amount):
    lowest_price = None
    print(target_amount)

    for ask_price, ask_amount in asks_data:
        ask_price = float(ask_price)
        ask_amount = float(ask_amount)

        if ask_amount >= target_amount:
            print("ask_price",ask_price,"ask_amount",ask_amount)
            if lowest_price is None or ask_price < lowest_price:
                lowest_price = ask_price

    return lowest_price

def find_lowest_price_coinbase(asks_data, target_amount):
    lowest_price = None

    for ask_price, ask_amount, _ in asks_data:
        ask_price = float(ask_price)
        ask_amount = float(ask_amount)

        if ask_amount >= target_amount:
            if lowest_price is None or ask_price < lowest_price:
                lowest_price = ask_price

    return lowest_price
