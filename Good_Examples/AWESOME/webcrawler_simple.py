# http://bytes.com/topic/python/answers/536816-need-write-simple-web-crawler
#webcrawler
#this is basically a shell, illustrating use of the "breath-first" type of webcrawler
# you have to add things for extracting the actual info from the webpage yourself
# all it currently do is to print the url of the pages, and the number of candidates to visit

import urllib

page = 'http://nytimes.com' # startpage
stack = []
stack.append(page)
visit = {} # keeps track of pages that we visited, to avoid loops
stopvar = 5 # I have added a variable that will allow you to exit after visiting x number of page,
#obviously we do not want to visit all page of the internet :)

while(stopvar >= 0):
    stopvar-=1
    cpage = stack.pop()
    f = urllib.urlopen(cpage)
    html=f.read()
    sp = "a href=\""
 
 # you want extract things from the html code (such as images, text etc, etc around here)
 # the rest of the thing is to extract hyperlinks, and put them into a stack, so we can
 # continue to visit pages

for i in range(len(html)):
    if(sp == html[i:i+len(sp)]):
        url = ""
        i+=len(sp)
    while(html[i] != "\""):
        url+=html[i]
        i+=1
# is our link a local link, or a global link? i leave local links as an exercise :)
    if(url[0:4] == "http"):
        if(visit.has_key(url) == False):
            stack.append(url)
            visit[url] = 1
print str(len(stack)) + " " + cpage
