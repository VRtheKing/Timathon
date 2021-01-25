import requests
from bs4 import BeautifulSoup
import webbrowser

res = requests.get('https://stackoverflow.com/')

def searchstack(q):
    return webbrowser.open(f'https://stackoverflow.com/search?q={q}')

#x = input('what is the error: ')
#x = x.replace(' ' ,'+')
#searchstack(x)
def searchonyt(x):
    return webbrowser.open(f'https://www.youtube.com/results?search_query={x}')

#x = input('what we should search on yt: ')
#x = x.replace(' ' ,'+')
#searchonyt(x)

def searchongoogle(x):
    return webbrowser.open(f'https://www.google.com/search?q={x}')

#x = x.replace(' ' ,'+')
#searchongoogle(x)
def start(x):
    if 'search' in x:
        x = x.replace('search','')
        searchongoogle(x)

    elif 'youtube' in x:
        x = x.replace('youtube','')
        searchonyt(x)

    elif 'stack' in x:
        x = x.replace('stack', '')
        searchstack(x)
