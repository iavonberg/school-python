from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://gizmodo.com/rss')
xml = BeautifulSoup(req, features='xml')

for item in xml.findAll('link'):
    url = item.text
    news = urllib.request.urlopen(url).read()
    print(news)
    print(20*'#')
