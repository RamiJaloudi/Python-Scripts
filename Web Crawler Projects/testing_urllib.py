
import urllib.request
import urllib.parse


# Watch this Video on YouTube: https://www.youtube.com/watch?v=5GzVNi0oTxQ
# x= urllib.request.urlopen('https://www.google.com')
# print(x.read())
# this will give the source code of google page.

'''
url = 'http://pythonprogramming.net'
values = {'s':'basic',
          'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
'''


'''-----------------------------------------
try:
    x = urllib.request.urlopen('https://wwww.google.com/search?q=test')

    print(x.read())

except Exception as e:
    print(str(e))
    
# when written as above, get HTTP Error 403: Forbidden
---------------------------------------------
'''

try:
    x = urllib.request.urlopen('https://wwww.google.com/search?q=test')

    headers = {}
    headers['User-Agent'] =
    print(x.read())

except Exception as e:
    print(str(e))

