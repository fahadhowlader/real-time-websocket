import requests
from celery import shared_task

@shared_task
def get_joke():
    url = 'http://api.icndb.com/jokes/random/'
    response = requests.get(url).json()
    joke = response['value']['joke']
    print(joke)
    return joke