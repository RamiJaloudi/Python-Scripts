import requests
from bs4 import BeautifulSoup

r = requests.get("http://nytimes.com")
# print r.content  # this will print out the content. This is why BS comes in handy.

soup = BeautifulSoup(r.content)
# print soup.prettify() # Gives a slightly better format.
# s = soup.find_all("a")
# print s


with open("the_links.csv", "w") as file:
    for link in soup.find_all("a"):
        # print link
        # link.get("href")
        # print link.get("href")
        # print link.text
        print link.get("href")
        file.write(link.get("href")+"\n")


'''
    #print link.get("href")
    file = open('the_links.txt', 'wb')
    file.write(link.get("href")+"\n")
    file.close()
'''
'''
    #the_page = link.get("href")
    SaveFile = open('page.txt', 'w')
    SaveFile.write(str(link.get("href")))
    SaveFile.close()
'''
    
    


