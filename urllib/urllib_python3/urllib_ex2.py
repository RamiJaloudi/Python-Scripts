import urllib.request
import re

url = 'http://www.pythonprgramming.net'
values = {'s':'basic',
          'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print (respData)

##paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
    print(eachP)

##    saveFile = open('withHeaders.txt','w')
##    saveFile.write(str(respData))
##    saveFile.close()

'''
except Exception as e:
    print(str(e))    
'''
