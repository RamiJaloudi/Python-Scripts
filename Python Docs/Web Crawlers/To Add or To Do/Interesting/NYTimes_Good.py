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

printTitle("Before start this journey ")

print """
If you are targeting public websites, try first looking for a official API,
use a well know service that provide the same data (you can for example, use several
google, yahoo, microsoft, etc... APIs to get web data). Review the terms of use of the site
and respect the robot.txt rules and in general, do this well.

Don't accept jobs for shaddy beahviour!
"""

printSubTitle("Get the webpage")
printExplain("You need to get the webpage is his raw HTML. This is the first step")
print "In python, the request library is the best today"
# http://runnable.com/Uri5rHtisU8kAA5S/command-the-web-with-python-requests-for-tutorial-beginner-http-scrapping-and-json

printSubTitle("Don't DDOS your target!")
# https://en.wikipedia.org/wiki/Denial-of-service_attack
print """
For testing, download to disk some test pages, so you don't hit the target
website. Beware of hit it too often, is not nice and can lead to ban your IP.
Behave well.
"""

printExplain("Prepare some utilities...")

printTitle("1- Get some test pages to analyze...")

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
saveReqToFile(getRequest("http://query.nytimes.com/search/sitesearch/#/drone+strikes"), 'nytimes.html')

# Actually read http://en.wikipedia.org/robots.txt

printExplain("Let's extract the section 'Topics in the news'")
print "And organize them using the linked categories"

printTitle("2- Read the HTML source code and look for interesting information")
print """
You need to know very well the HTML language. Plus, remember you can't
trust that the same info you want will be there later. HTML is *messy*, have
not structure, can change anytime.
"""

print "Visit the URL and use a web inspector to locate 'Topics in the news'"
# https://developer.apple.com/safari/tools/
# https://developers.google.com/chrome-developer-tools/ 
# https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector

print """
With that, you will see that 'Topics in the news' is enclosed in a <table>,
Unfortunally for us have no id. neither class. We will need to get the div with
id=mw-content-text (his wrapper) and pick the 3 table child and pray it to be
our headline. The first <tr> is for 'Topics in the news, the 2d have the actual
news, in a <ul> and each <li> have the news.

Then inside each news you get several links <a>, where the title will serve as our
category.

That is for the headlines.
"""

printExplain('Relevant HTML structure:')
print """
<div class="mw-content-ltr" dir="ltr" id="mw-content-text" lang="en">
....
....
 <table style="padding: 5px; width:100%; background-color: #f5faff; border:1px solid #cedff2; margin-bottom:7px">
....
....
      Worldwide current events
....
....
 <table style="width: 100%; margin-bottom:7px; border:1px solid #cedff2; padding:2px; background-color:#f5faff">
  <tr bgcolor="#CEDFF2">
....
....
    Topics in the news
....
....
  <tr>
....
....
    <ul>
....
....
     <li>
      In <a href="/wiki/Handball" title="Handball"> handball</a>, the
....
....
     </li>
....
....
"""

print """
Then you have several tables with class="vevent", by date, and them have
deep down in the td with class='description' several <dl> (the headline)
then <ul> with the actual news
"""

printExplain('Relevant HTML structure:')
print """
   <table class="vevent" style="width:100%; margin:7px 0px; padding:2px; background-color:white; border:1px #cef2e0 solid;">
    <tr>
...
...
    <tr>
...        Armed conflicts and attacks
...      <ul>
       <li>
        <a href="/wiki/Iraqi_insurgency_(post-U.S._withdrawal)" title="Iraqi insurgency (post-U.S. withdrawal)">
         Iraqi insurgency (post-U.S. withdrawal)
        </a>
...
...
        <ul>
         <li>
          A <a href="/wiki/Car_bomb" title="Car bomb">car bomb</a> explodes near a church as
...         </li>
        </ul>
...
...
"""

printTitle("3- Extract the data with Beautiful Soup")

printExplain("I will build a dict with category= list of stories")

print """
You could think: Let's use several regex. Remove that from your mind.

Regex are not the rigth tool here. You need a HTML parser, period.

Beautiful Soup is the most popular one for python.
"""

from bs4 import BeautifulSoup
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/

printExplain("Load the HTML file...")

with open(getFilePath('wikinews.com.html'), 'r') as f:
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


printExplain("Now, let's extract the daily news...")
print "Grab all the tables with class=vevent"


def filterTable(table):
    classes = table.get('class')

    if classes:
        return 'vevent' in classes
    else:
        return False


# Filter for the tables with vevent
tableEvents = (x for x in tables if filterTable(x))

print """
We have 2 kind of new headline.

The first, is a URL link to a main topic, then the actual news.
The other is just the new.
"""

# Set recursive=False to get only the first level of tags. If is True,
# It will get all the tags below the tree, complicating the logic to
# separate the 2 kinds of news...
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
