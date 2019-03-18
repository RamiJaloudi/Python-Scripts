#! /usr/sfw/bin/python
import urllib
import re
import pickle
worddict={}
page = "http://nytimes.com" #startpage
stack = []
stack.append(page)
visit = {} # keeps track of pages that we visited, to avoid loops
stopvar = 500
while(stopvar >= 0):
  stopvar-=1
  print stopvar
  cpage = stack.pop(0)
  try:
    f = urllib.urlopen(cpage)
    html = f.read()
    #print html
  except:
    print cpage,"Unexpected Error"
    continue
  sp = "a href=\""
  htmlvisibletext = re.sub('<.*?>','',html)
  htmlvisibletext = re.sub('[^a-zA-z ]','',htmlvisibletext)
  words=htmlvisibletext.split()
  for word in words:
    word=word.lower()
    if(word not in worddict):
      dict={cpage:1}
      worddict[word]=dict
    else:
      dict=worddict[word];
  for i in range(len(html)):
 
    if(sp == html[i:i+len(sp)]):
      url = ""
      i+=len(sp)
      while(html[i] != "\""):
        url+=html[i]
        i+=1
      if(url[0:4] == "http"):
        if(visit.has_key(url) == False):
          visit[url]=1
          stack.append(url)
for key in worddict:
  items = [(v, k) for k, v in worddict[key].items()]
  items.sort()
  items.reverse()
  worddict[key] = [(k, v) for v, k in items]
dumpfile = open('dictdump','wb')
pickle.dump(worddict,dumpfile)
