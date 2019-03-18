import urllib
import urlparse
import re
import urlparse

##x = urllib.urlopen('http://www.google.com')
##print x.read()

url = 'http://www.pythonprgramming.net'
values = {'s':'basic',
          'submit':'search'}

data = urlparse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print (respData)

##paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
    print(eachP)



