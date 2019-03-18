#!/usr/bin/python
#
# Author: Brock Hargreaves
# Date: May 2014
# 
# Multiprocess and trimmed version of the crawler/fetcher queue based implementation of James Mills:
#
# http://code.activestate.com/recipes/576551-simple-web-crawler/?in=user-4167757
 
import requests
import urlparse
import re 
from multiprocessing import Queue, Manager, Process, Lock, Value
from bs4 import BeautifulSoup
from cgi import escape
import os
 
class Crawler(Process):
    def __init__(self, root, depth, queue, myList, counter, links, followed):
        super(Crawler, self).__init__()
        self.root     = root
        self.depth    = depth
        self.urls     = [] # Empty list, used to keep track of the urls of a single page
        self.host     = urlparse.urlparse(root).netloc
        self.links    = links
        self.followed = followed
        self.q        = queue
        self.myList   = myList
        self.counter  = counter
    
    def run(self):
        if hasattr(os, 'getppid'):  # only available on Unix
            print "Process %i is now running with parent process %i" % (os.getpid(), os.getppid())
        page = Fetcher(self.root)
        page.fetch()
        self.myList.append(self.root) #List with the single element self.root, ie: the root url
        
        for url in page.urls:
            self.q.put(url)
        
        while True:
        
            try:
                # Timeout, i.e., None of the other processes have put anything onto the queue in 2 seconds
                url = self.q.get(timeout=2) 
            except Exception:
                print "Queue timed out, leaving crawler"
                break
                
            with self.counter.get_lock():
                self.counter.value += 1
                #print "self.counter.value = %i" % self.counter.value #Debugging
            
            if url not in self.myList:
                print "Process %i is adding url: %s" % (os.getpid(), url)
                self.myList.append(url)
                
                try:
                    
                        
                    host = urlparse.urlparse(url).netloc
 
                    if re.match(".*%s" % self.host, host): # For now, only crawl within a single domain
                        with self.followed.get_lock():
                            self.followed.value += 1
                        print "Process %i is crawling url: %s" % (os.getpid(), url)
                        page = Fetcher(url)
                        page.fetch()
                        for i,url in enumerate(page): # enumerate(page) returns a 2-tuple, thus 'i' is a dummy variable to store that value
                            if url not in self.urls:
                                with self.links.get_lock():
                                    self.links.value += 1
                                    
                                self.q.put(url)
                                self.urls.append(url)
                                
                                with self.counter.get_lock():
                                    if self.counter.value > self.depth and self.depth > 0:
                                        print "Reached max depth, leaving crawler"
                                        break
                    #else:
                        #print "url: %s is not in the domain: %s" % (url, self.host) # Debugging
                               
                except Exception as e:
                    print "ERROR: Can't process url '%s' (%s)" % (url, e)
            #else:
                #print "url: %s has already been followed" % url   # Debugging             
                
class Fetcher(object):
    def __init__(self,url):
        self.url = url
        self.urls = []
        
    # An object can be iterated over with "for" if it implements
    # __iter__() or __getitem__(). We require this for our Crawler.crawl()
    
    def __getitem__(self, x):  
        return self.urls[x]   
        
    def fetch(self):
        try:
            request = requests.get(self.url)
            request.raise_for_status()
        except Exception as e:
            print "For url: %s, Exception: %s " % (self.url,e)      
        
        soup = BeautifulSoup(request.text)
        tags = soup('a')
        
        # Identify unique links
        for tag in tags:
            href = tag.get("href")
 
            if href is not None:
                url = urlparse.urljoin(request.url,escape(href))
        
                if url not in self.urls:
                    self.urls.append(url)
                 
def main():
    # Put the manager in charge of how the processes access the list
    mgr = Manager()
    myList = mgr.list() 
    
    # FIFO Queue for multiprocessing
    q = Queue()
    
    # Test site and arguments
    url = "http://nytimes.com" 
    depth = 3
    counter = Value('i', 0) # Need to use a lock to ensure we update a counter correctly
    links   = Value('i', 0) # Same reason as counter
    followed = Value('i',0) # ....
    
    # Start and keep track of processes
    procs = []
    for i in range(4):
        p = Crawler(url,depth, q,myList, counter, links, followed)
        procs.append(p)
        p.start()
    
    # Ensure processes terminate properly    
    for p in procs:
        p.join()    
            
    for i,item in enumerate(myList):
        print "%i: %s" % (i,item)   
 
    print "Found:    %i" % links.value
    print "Followed: %i" % followed.value
    
        
if __name__ == "__main__":
    main()       
                

