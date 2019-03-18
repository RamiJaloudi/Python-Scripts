import urllib
import re

urls=["http://google.com","https://facebook.com","http://reddit.com"]

i=0

##these_regex="<title>(.+?)</title>"
these_regex="<title.*?>(.+?)</title>"
pattern=re.compile(these_regex)

while(i<len(urls)):
        htmlfile=urllib.urlopen(urls[i])
        htmltext=htmlfile.read()
        titles=re.findall(pattern,htmltext)
        print titles
        i+=1
