import requests
from bs4 import BeautifulSoup

res = requests.get('https://stackoverflow.com/')


soup = BeautifulSoup(res.text, 'html.parser')
searchbar = soup.find('form', id = 'search')
searchbar.