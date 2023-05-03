from bs4 import BeautifulSoup
import urllib.request
import time

req = urllib.request.urlopen('https://gizmodo.com/rss')
xml = BeautifulSoup(req, features='xml')

for item in xml.findAll('link'):
    url = item.text
    news = urllib.request.urlopen(url).read()
    
    page = BeautifulSoup(news)

    for p in page.findAll('p'):
        print(p.text)

    time.sleep(10)
