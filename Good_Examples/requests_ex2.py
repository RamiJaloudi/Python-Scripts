import requests

##Saving Downloaded Files to the Hard Drive
##From here, you can save the web page to a file on your hard drive with the standard open()
##function and write() method. There are some slight differences, though. First, you must open
##the file in write binary mode, by passing the string 'wb' as the second argument to open(). Even
##if the page was in plaintext (such as the Romeo and Juliet text you downloaded earlier), you need
##to write binary data instead of text data in order to maintain the Unicode encoding of the text.
##
##To write the web page to a file, you can use a for loop with the response value’s
##iter_content() method. The iter_content() method will return “chunks” of the content on
##each iteration through the loop. Each chunk is of the bytes data type, and you get to specify how
##many bytes each chunk will contain. One hundred thousand bytes is generally a good size, so
##pass 100000 as the argument to iter_context():

res = requests.get('http://www.nytimes.com/pages/technology.txt')
print type(res)

# to see if the download succeeded
print res.status_code == requests.codes.ok

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

print len(res.text)

playFile = open('res_iter_content.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
    playFile.close()

print chunk


