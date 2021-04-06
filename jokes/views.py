from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    url = 'http://api.icndb.com/jokes/random/'
    response = requests.get(url).json()
    jokes = response['value']['joke']
    return render(request, 'index.html', context={'text': jokes})