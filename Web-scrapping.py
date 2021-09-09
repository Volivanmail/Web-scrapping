import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re


KEYWORDS  = ['дизайн', 'фото', 'web', 'python', 'linux', 'java']

URL = 'https://habr.com'
response = requests.get('https://habr.com/ru/all/')

response.raise_for_status()

soup = BeautifulSoup(response.text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    snippets = article.find_all('div', class_='tm-article-snippet')
    snippets = [snippet.text for snippet in snippets]
    snipets = snippets[0]
    snippets = re.findall("\w+", snipets.lower())
    for keyword in KEYWORDS:
        if keyword in snippets:
            date = article.find ('time')
            title = article.find('h2')
            href = title.find('a').attrs.get('href')
            print(date.text, title.text, URL + href)