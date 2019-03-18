import urllib2
request = urllib2.Request('http://python.org/')
request.add_header("User-Agent", "Mozilla") # Specify User Agent
opener =urllib2.build_opener()
response =opener.open(request)
html = response.read()

#print html
#print html.split('\n')[0] #<!doctype html>
#print html.split('\n')
print request.info()

# Here, I had to create another response "response2" b/c .Request does not work.
response2 = urllib2.urlopen('http://python.org/')
print response2.info() #Getting the HTTP headers


