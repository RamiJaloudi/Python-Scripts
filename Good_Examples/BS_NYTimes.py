# <p class="myforecast-current-lrg">53&deg;F</p>
import requests, bs4

res = requests.get('http://nytimes.com')

try:
    res.raise_for_status()
except Exception as exc:
        print "Status is %s is:" % exc
        

soup = bs4.BeautifulSoup(res.text)


elems = soup.prettify
elems_pr = soup.select('h2')

for h in elems_pr:
    try:
        print elems_pr[0].getText()
        print elems_pr[0].get("href")
        print '\n'
        elems_pr.pop(0)
    except:
        continue


    
with open("the_links.csv", "w") as file:
    for link in soup.find_all("a"):
        # print link
        # link.get("href")
        # print link.get("href")
        # print link.text
        print link.get("href")
        print link.Text
        file.write(link.get("href")+"\n")
        

##print elems
##print type(elems)

##print len(elems)
###print type(elems[0])


#print str(elems)
#print elems[0].attrs



