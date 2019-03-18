import urllib
from bs4 import BeautifulSoup
import re

url = 'https://nytimes.com'

request = urllib.urlopen(url)
response = request.read()

soup = BeautifulSoup(response)

'''
for tag in soup:
    # tag = soup.div
    tag = soup.a
    #type(tag)
    # <class 'bs4.element.Tag'>
    print tag
    print tag.name
    print tag.attrs
    print '\n\n\n'
'''

#print soup.find_all('a', href=True)


##head_tag = soup.head
##print head_tag
### <head><title>The Dormouse's story</title></head>
##print '\n\n\n'
##print head_tag.contents
###[<title>The Dormouse's story</title>]
##
##title_tag = head_tag.contents[0]
##print title_tag
##print '\n\n\n'
### <title>The Dormouse's story</title>
##
##print title_tag.contents
### [u'The Dormouse's story']
##text = title_tag.contents[0]
##print text.contents
##
##for child in title_tag.children:
##    print(child)


##print(soup.html.string)
##
##for string in soup.strings:
##    print(repr(string))


##for string in soup.stripped_strings:
##    print(repr(string))


##print soup.find_all('b')


##for tag in soup.find_all(re.compile("^b")):
##    print(tag.name)


### This code finds all the tags whose names contain the letter ‘t’:
##for tag in soup.find_all(re.compile("t")):
##    print(tag.name)
# html
# title



##print soup.find_all("title")
### [<title>The Dormouse's story</title>]


##print soup.find_all("p", "title")
### [<p class="title"><b>The Dormouse's story</b></p>]
##
##
##
##soup.find_all("a")
### [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
### <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
### <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


##soup.find_all(id="link2")
### [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]



##searched = soup.find(text=re.compile("The"))
##print searched

#If you pass in a value for href, Beautiful Soup will filter against each tag’s ‘href’ attribute:
print soup.find_all(href=re.compile("The"))
