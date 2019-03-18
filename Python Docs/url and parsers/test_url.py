import urllib.request

try:
    req = urllib.request.Request('http://google.com')
    response = urllib.request.urlopen(req)
    the_page = response.read()
    print (the_page)
    SaveFile = open('the_page.txt', 'w')
    SaveFile = write(str(the_page))
    SaveFile.close()

except Exception as e:
    print(str(e))
    
