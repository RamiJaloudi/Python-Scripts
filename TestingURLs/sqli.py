import urllib
import re

#url = raw_input('Enter - ')

html = urllib.urlopen('http://hackthissite.org')

resp = html.read()

#print(html.read())


#ONLY RUN THIS ON SANDBOX SITES. NEED TO FIX THIS. MESSY!!!
#REVIEW URLLIB & FIND THE EQUIV OF "FINDALL" OR THE CORRECT USAGE. 

links = resp.find('href="(http://.*?)"', resp)



'''
x = 0

for link in links:
    x = x + 1
    print link

print x

#fullybody = body.decode('utf-8')

if "You have an error in your SQL syntax" in fullbody:
	print("Classically vulnerable")
else:
	print("Back off")
'''
