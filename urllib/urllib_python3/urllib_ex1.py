import urllib.request

"""
x = urllib.request.urlopen('http://www.google.com')
print(x.read())
"""

"""
url = 'https://pythonprgramming.net'
values = {'s':'basic',
          'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print (respData)
"""

"""
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x(read())

except Exception as e:
    print(str(e))
"""

try:
    url = 'https://www.google.com/search?q=test'

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))    
