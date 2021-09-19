import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

URL = 'https://habr.com'
response = requests.get('https://habr.com/ru/all/')

response.raise_for_status()

soup = BeautifulSoup(response.text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    title = article.find('h2')
    href = title.find('a').attrs.get('href')
    response = requests.get(URL + href)
    soup = BeautifulSoup(response.text, features='html.parser')
    text = str(soup)
    for keyword in KEYWORDS:
        if keyword in text:
            date = article.find ('time')
            title = article.find('h2')
            href = title.find('a').attrs.get('href')
            print(f'тег {keyword} - ', date.text, title.text, URL + href)
