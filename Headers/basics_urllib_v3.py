import urllib.request # this is a GET
import urllib.parse

# urlparse Module - urlparse(urlstr, defProtSCh=None, allowFrag=None)
# urlparse() breaks a URL into a 6-tuple (prot_sch, net_loc, path params, query, frag)
# defProtSh indidcates a default network protocol or download scheme in case one is not provided in urlstr.
# allFrag is a flag that signals whether or not a fragment part of a URL is allowed.

''' 1st EXERCISE
x = urllib.request.urlopen('http://google.com')
print(x.read())
'''

''' 2nd EXERCISE  
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

# 3rd EXERCISE
'''
try:
    x = urllib.request.urlopen('https://google.com/search?=test')
    print(x.read())
except Exception as e:
    print(str(e))
# This was supposed to throw a 403 Exception, which I did not get.
# Create Agent assumming the above occurred.
'''

# 4th EXERCISE
try:
    url = 'http://www.informit.com/'
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
# After running this script, you will find the text file saved in the same folder of this script.

'''
For alternative value for "headers['User-Agent']", see below:
ua.ie
# Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);
ua.msie
# Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)'
ua['Internet Explorer']
# Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)
ua.opera
# Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11
ua.chrome
# Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
ua.google
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13
ua['google chrome']
# Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11
ua.firefox
# Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1
ua.ff
# Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1
ua.safari
# Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25
'''
