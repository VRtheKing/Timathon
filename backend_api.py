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

def findsynonyms(x):
    file = requests.get(f'https://www.google.com/search?q={x}')
    soup = BeautifulSoup(file.text, 'html.parser')
    div = soup.find('div')
    print(div)

def searchamazon(x):
    return webbrowser.open(f'https://www.amazon.in/s?k={x}')

def searchflip(x):
    return webbrowser.open(f'https://www.flipkart.com/search?q={x}')

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
    elif 'Amazon find' in x:
        x = command.replace('Amazon find', '')
        return searchamazon(x)

    elif 'Flipkart find' in x:
        x = command.replace('Flipkart find', '')
        return searchflip(x)
