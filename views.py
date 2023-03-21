import requests
from django.shortcuts import render

def crypto_list(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    response = requests.get(url)
    cryptos = response.json()
    return render(request, 'crypto/crypto_list.html', {'cryptos': cryptos})





# class CryptoAPI(APIView):
#     

#     def get(self, request):
#         url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
#         response = requests.get(url)
#         data = response.json()
#         return Response(data)
