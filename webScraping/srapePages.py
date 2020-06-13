from bs4 import BeautifulSoup
import requests

 url = 'https://scrapingclub.com/exercise/list_basic/'
 resp = requests.get(url)
 soup = BeautifulSoup(resp.text, 'lxml')
 items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
 count = 1   
 for i in items:
     itemName = i.find('h4', class='card-title').text.strip('\n')
     itemPrice = i.find('h5').text
     print(f'{count}")" Price: {itemPrice}, Item name {itemName}')
     count += 1

pages = soup.find_all('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum !=None:
        x = link.get('href')
        urls.append(x)
count = 1
for i in urls:
    newUrl = url + i
    resp = requests.get(newUrl)
    soup = BeautifulSoup(resp.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    
    for i in items:
        itemName = i.find('h4', class='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print(f'{count}")" Price: {itemPrice}, Item name {itemName}')
        count += 1