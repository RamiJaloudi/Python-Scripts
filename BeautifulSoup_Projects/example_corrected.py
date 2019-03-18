import urllib
from urllib import urlopen
from bs4 import BeautifulSoup
import re

url = "http://nytimes.com"
webpage = urllib.urlopen(url)
webcontent = webpage.read()
#print webcontent

# Grab everything the lies between the title tags using a REGEX
patFinderTitle = re.compile(r'<title>(.*?)</title>')

# Grab the link to the original article using REGEX
patFinderLink = re.compile(r'<link rel.*href="(.*)" />')

#Store all of the titles and links found in 2 lists
findPatTitle = re.findall(patFinderTitle, webcontent)
findPatLink = re.findall(patFinderLink, webcontent)

#Create an interator that will cycle through the first 16 articles and skip a few
#listIterator = []
#listIterator[:] = range(1, 1000)

# Print out the results to screen
#for i in listIterator:
print findPatTitle # The link to the original article
print '\n'
print findPatLink # The link to the original article
    
