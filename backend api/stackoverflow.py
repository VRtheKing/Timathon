import requests
from bs4 import BeautifulSoup
import webbrowser

res = requests.get('https://stackoverflow.com/')

def searchstack(q):
    res =  requests.get(f'https://stackoverflow.com/search?q={q}')
    result = BeautifulSoup(res.content , 'html.parser')
    question_and_answers = result.find_all('div', {'class':'question-summary search-result'})
    print(question_and_answers)

x = input('what is the error: ')
x = x.replace(' ' ,'+')
searchstack(x)
