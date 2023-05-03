from bs4 import BeautifulSoup
import time
import urllib.request
from dbconnect import connection

req = urllib.request.urlopen('https://gizmodo.com/rss')

xml = BeautifulSoup(req, features='xml')

c, conn = connection()

def parse_links():
    for item in xml.findAll('link'):
        url = item.text

        c.execute("SELECT * FROM links WHERE link = (%s)", [url])

        rows = c.fetchall()

        if len(rows) == 0: 
            c.execute("INSERT INTO links (time, link) VALUES (%s, %s)",
                    (time.time(), url))
            conn.commit()
            print("Found a new link!")
        else:
            print('Link already exists')

        time.sleep(10)

while True:
    parse_links()
