import requests 
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'

response = requests.get(url+'?page=1' )
soup = BeautifulSoup(response.text, 'lxml')

item = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for i in item:
    itemName = i.find('h4', class_ ='card-title').text
    itemPrice = i.find('h5').text
    count = count + 1
    print('%s) price: %s, item names: %s'% (count,itemPrice, itemName))

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

for link in links:
    #print(link.text)
    #print(link.text.isdigit())
    pageNum = int(link.text) if link.text.isdigit() else None
    
    print(pageNum)
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
for i in urls:
    newURL = url + i
    print(newURL)
    response = requests.get(url+i)
    soup = BeautifulSoup(response.text, 'lxml')
    item = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')  
    
    for i in item:
       
        itemName = i.find('h4', class_ ='card-title').text
        itemPrice = i.find('h5').text
        count = count + 1
        print('%s) price: %s, item names: %s'% (count,itemPrice, itemName))

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')