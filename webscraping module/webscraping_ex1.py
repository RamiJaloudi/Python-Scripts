from webscraping import download, xpath
D = download.Download()
url = 'http://uslawfirms.co'
html1 = D.get(url)
html2 = D.archive_get(url)
for html in (html1, html2):
    print xpath.get(html, '//title')
