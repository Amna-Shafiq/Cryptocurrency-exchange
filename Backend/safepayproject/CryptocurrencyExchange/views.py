from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services.fetch_order_books_service import ExchangeAPIService

@api_view(['GET'])
def exchange_rate(request):
    try:
        amount = float(request.GET.get('amount', 0))
    except ValueError:
        return Response({'error': 'Invalid amount provided'}, status=400)

    if amount <= 0:
        return Response({'error': 'Amount must be greater than zero'}, status=400)

    service = ExchangeAPIService()

    try:
        binance_data = service.get_binance_data()
        coinbase_data = service.get_coinbase_data()
    except ValueError as e:
        return Response({'error': str(e)}, status=500)

    binance_data_asks = binance_data.get("asks", [])
    coinbase_data_asks = coinbase_data.get("asks", [])

    binance_price = service.find_lowest_price_binance(binance_data_asks, amount)
    coinbase_price = service.find_lowest_price_coinbase(coinbase_data_asks, amount)

    best_price = min(filter(None, [binance_price, coinbase_price]))

    response_data = {
        'binance_price': binance_price,
        'coinbase_price': coinbase_price,
        'best_price': best_price
    }

    return Response(response_data)