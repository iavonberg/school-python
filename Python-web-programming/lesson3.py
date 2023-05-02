import urllib.request
import urllib.parse

# req = urllib.request.urlopen('https://www.google.com')
# print(req.read())

url = 'https://www.google.com/search?q='
values = {
    'q':'python programming tutorials'
}

data = urllib.parse.urlencode(values)
url = 'https://www.google.com/search?'+data
# data = data.encode('utf-8')

headers = {

}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)