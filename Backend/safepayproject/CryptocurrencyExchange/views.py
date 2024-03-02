from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def exchange_rate(request):
    exchange_rate_value = 1.5
    return Response({'exchange_rate': exchange_rate_value}) #this is returning a json