import requests 
from bs4 import BeautifulSoup


url = 'http://quotes.toscrape.com/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text,'lxml')
print(soup)

quotes = soup.find_all('span', class='text')
auth = soup.find_all('small', class='author')
tags = soup.find_all('small', class='tags')



for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(auth[i].text)
    quoteTags = tagsp[i].find_all('a', class='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)