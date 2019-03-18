# -*- encoding: utf-8 -*-
# Made by http://www.elmalabarista.com
# This will teach about the steps for web scraping a web site

# REQUISITES
#

# This is for python 2.7 (However, not much change for python 3.0+).
# Basic understanding of programing, use of variables and control flow,
# HTML & web development in general

# About

# Web scraping is the basic of a web search engine. Is the task of get &
# evaluate the content of a web page and extract the information of it

# Important:
# Web scraping done rigth is HARD. This tutorial just show the basics of it.
# Use a proper framework as scrapy (below) and understand the tecnical &
# (possible) legal rammifications. This is just about the extraction of
# data, not about cralwers/robots.

# Usefull links
# https://en.wikipedia.org/wiki/Web_scraping
# http://scrapy.org/
# http://www.crummy.com/software/BeautifulSoup/
# http://blog.hartleybrody.com/web-scraping/
# http://www.slideshare.net/TheVirendraRajput/web-scraping-in-python
# http://www.robotstxt.org/

import os
import requests

from utils import printTitle, printSubTitle, printExplain, printTab

CURRENT_DIR = os.path.dirname(__file__)
TESTDATA_DIR = os.path.join(CURRENT_DIR, 'test')


def setupTestData():
    if not os.path.exists(TESTDATA_DIR):
        os.makedirs(TESTDATA_DIR)


def getFilePath(fileName):
    return os.path.join(TESTDATA_DIR, fileName)


def saveReqToFile(req, fileName):
    printTab("Saving %s to %s" % (req.url, fileName))

    setupTestData()
    #Save to file the content of request...
    theFile = getFilePath(fileName)
    with open(theFile, 'wb') as f:
        # Is possible to do f.write(theFile.content)
        # However, this is the recommend way for (possible) large responses
        # Write in chunks... I decide in 512.
        # http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
        for chunk in req.iter_content(512):
            f.write(chunk)


def getRequest(url):
    return requests.get(url, stream=True)


# This is the source of our sample page
# Uncomment to get the online data. This could broke the code, if the HTML change
# from the time this tutorial is made
# saveReqToFile(getRequest("https://en.wikipedia.org/wiki/Portal:Current_events"), 'wikinews.com.html')
saveReqToFile(getRequest("http://leagle.com/decisions/latest/New%20Jersey"), 'leagle.com.html')

# Actually read http://en.wikipedia.org/robots.txt



from bs4 import BeautifulSoup
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/

printExplain("Load the HTML file...")

with open(getFilePath('leagle.com.html'), 'r') as f:
    soup = BeautifulSoup((f))


#print "The title of the page is: ", soup.title.string
print unicode(soup.title.string)

printSubTitle("Extract the headline..")

divContent = soup.find(id="mw-content-text")

tables = divContent.find_all('table', recursive=False)

print "Inside mw-content-text exist %d tables" % len(tables)
print "Get the 2 table, it have the news.."
tableHeadline = tables[1]  # The third

print "Get all the <li> tags"
tableNews = tableHeadline.find_all("li")

# My structure
news = {}


def processNews(listOfli):
    for new in listOfli:
        for category in new.find_all('a'):
            title = category.get('title')
            #If don't have title is because is a external link
            #to the source of the new. I discard this...
            if title is None:
                continue

            if title in news:
                news[title].append(new.text)
            else:
                news[title] = [new.text]


processNews(tableNews)


def filterTable(table):
    classes = table.get('class')

    if classes:
        return 'vevent' in classes
    else:
        return False


# Filter for the tables with vevent
tableEvents = (x for x in tables if filterTable(x))

for event in tableEvents:
    ulNew = event.find_all("tr")[2].td.find_all('ul', recursive=False)

    for ul in ulNew:
        for li in ul.find_all('li', recursive=False):
            subUls = li.find_all('ul')
            # Is a headline + new(s)?
            if len(subUls):
                for subUl in subUls:
                    processNews(subUl.find_all('li'))
            else:
                # Is a normal headline
                processNews([li])

for category in sorted(news):
    headlines = news[category]

    printSubTitle(category.encode('ascii', 'ignore'))

    for headline in headlines:
        printTab(headline.encode('ascii', 'ignore'))
        print
