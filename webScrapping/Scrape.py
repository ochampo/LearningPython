import requests 
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text,'lxml')

print(soup)

qoutes = soup.find_all('span', class_ = 'text')

print(qoutes)

for qoute in qoutes:
    print(qoute.text)

authors = qoutes.find_all('small', class_='author')