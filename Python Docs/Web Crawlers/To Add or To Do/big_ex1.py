# -*- coding:utf-8 -*-
# myspider.py
# Tanky Woo

import urllib
import threading
from Queue import Queue
from sgmllib import SGMLParser
from optparse import OptionParser
import sqlite3
import logging
import re
import os
import stat

# Parser for command line options
def cmdParser():
    usage = "usage: %prog [options] arg"
    cmdLine = OptionParser(usage=usage, version="%prog 1.0")
    cmdLine.add_option("-u", "--url", action="store", dest="siteUrl", type="string",
                       help=u"the website's url")
    cmdLine.add_option("-d", "--deep", action="store", dest="depthNum", type="int",
                       default="3", help=u"the depth of crawler，default is 3")
    cmdLine.add_option("-t", "--thread", action="store", dest="threadNum", type="int",
                       default="10", help=u"the number of the thread，default is 10")
    cmdLine.add_option("-v", "--level", action="store", dest="logLevel", type="int",
                       default="0", help=u"the level of the logfile, default is 5")
    cmdLine.add_option("-l", "--logfile", action="store", dest="logFile", type="string",
                       default="spider.log", help=u"the name of the logfile, default is spider.log")

    (options, args) = cmdLine.parse_args()
    return options

# Initialize the log file
def logInit(logfile="spider.log", level=5, quiet=False):
    logger = logging.getLogger()
    # 0~5 level
    # level 0 -- CRITICAL -- 50
    # level 1 -- ERROR -- 40
    # level 2 -- WARNING -- 30
    # level 3 -- INFO -- 20
    # level 4 -- DEBUG -- 10
    # level 5 -- NOTSET -- 0
    logger.setLevel(50-level*10)
    hdlr = logging.FileHandler(logfile)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    # if the quiet equal False, then output the log information in the standard stream also
    if not quiet:
        hdlr = logging.StreamHandler()
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
    return logger


class Node:
    def __init__(self, deep, url):
        self.url = url
        self.deep = deep


# the urlParser class
# parser the link in the web page and store in the url list
class urlParser(SGMLParser):
    def reset(self):
        self.urls = []
        SGMLParser.reset(self)
    # get the link which begin with "href"
    def start_a(self, attrs):
        href = [v for k, v in attrs if k == 'href']
        if href:
            self.urls.extend(href)

# A mult-thread class
# read the url
class readUrlThread(threading.Thread):
    # deep is the depth of the crawler
    def __init__(self, urlque, htmlque, deep):
        threading.Thread.__init__(self)
        self.urlque = urlque
        self.htmlque = htmlque
        self.deep = deep

    def getUrl(self, node):            
        try:
            headers = {} # added by RJ
			headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64 rv:16.0.0) Gecko/20121011 Firefix/16.0.1' # added by RJ
			htmlSource = urllib.urlopen(node.url, headers=headers).read() # modified slightly by RJ
        except UnicodeError, e: # if there is a Unicode exception, switch and put back to the queue
            self.urlque.put(Node(node.deep, node.url.encode('raw_unicode_escape')))
            mylog.error("unicode error" + e)
            return None
        except Exception, e:
            mylog.error("crawl error" + str(e), )
            return None

        self.htmlque.put((node.url, htmlSource))

        print "get url: " + node.url
        mylog.info("get url: " + node.url)

        if node.deep <= self.deep:  
            parser = urlParser()
            parser.feed(htmlSource)
            for url in parser.urls:
                myurl = url
                self.urlque.put(Node(node.deep+1, myurl))
        return htmlSource

    def run(self):
        while True:
            node = self.urlque.get()
            htmlSource = self.getUrl(node)
            self.urlque.task_done()

class writeDatabaseThread(threading.Thread):
    def __init__(self, htmlque, sqlfile):
        threading.Thread.__init__(self)
        self.htmlque = htmlque
        self.sqlfile = sqlfile

    def run(self):
        conn = sqlite3.connect(self.sqlfile)
        conn.text_factory = str
        cursor = conn.cursor()

        cursor.execute('''
        create table data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url text,
            html text
        )
        ''')

        conn.commit()

        print 'Begin<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
        while True:
            url, html = self.htmlque.get()
            self.htmlque.task_done()
            try:
                # insert the data into the database
                cursor.execute('insert into data (url, html) values(?, ?)', (url, html))
                conn.commit()
                mylog.info("Write to: " + url)
                print u'Write to: ', url, self.htmlque.qsize()
            except Exception, e:
                mylog.error("database error: " + e)
                print 'database error: ', e
                self.htmlque.put((url, html))

        #############################################
        # This statement was not be printed, why??? #
        #############################################
        print u'End<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
        cursor.close()
        conn.close()


def work(url, deep, threads, dbfile):

    urlque = Queue(0)
    htmlque = Queue(0)

    # if the dbfile is exist, remove it
    if os.path.isfile(dbfile):
        os.chmod(dbfile, stat.S_IWRITE)
        os.remove(dbfile)

    # read url from the urlque and parser it
    for i in range(threads):
        r = readUrlThread(urlque, htmlque, deep)
        r.setDaemon(True)
        r.start()

    urlque.put(Node(1, url))

    # store the html source into the database
    w = writeDatabaseThread(htmlque, dbfile)
    w.setDaemon(True)
    w.start()

    urlque.join()
    htmlque.join()
    print u'Done...'

if __name__ == '__main__':
    options = cmdParser()
    mylog = logInit("spider.log", 5)
    work('http://nytimes.com', 5, 100, "data.db")
