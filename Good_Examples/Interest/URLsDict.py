import urllib, threading

class Crawler(threading.Thread):

    global g_URLsDict 
    varLock = threading.Lock()
    count = 0

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.url = self.queue.get()

def run(self):
    while 1:
        print self.getName()+" started"
        url = self.queue.get() # <-- note that we're blocking here to wait for a url from the queue
        self.page = getPage(url)
        self.parsedPage = getParsedPage(self.page, fix=True)
        self.urls = getLinksFromParsedPage(self.parsedPage)

        for url in self.urls:

            self.fp = hashlib.sha1(url).hexdigest()

            #url-seen check
            Crawler.varLock.acquire() #lock for global variable g_URLs
            if self.fp in g_URLsDict:
                Crawler.varLock.release() #releasing lock
            else:
                #print url+" does not exist"
                Crawler.count +=1
                print "total links: %d"%len(g_URLsDict)
                print self.fp
                g_URLsDict[self.fp] = url
                Crawler.varLock.release() #releasing lock
                self.queue.put(url)

                print self.getName()+ " %d"%self.queue.qsize()

        self.queue.task_done() # <-- We've processed the url this thread pulled off the queue so indicate we're done with it


print g_URLsDict
queue = Queue.Queue()
queue.put("http://www.ertir.com")

for i in range(5):
    t = Crawler(queue)
    t.setDaemon(True)
    t.start()

queue.join()
