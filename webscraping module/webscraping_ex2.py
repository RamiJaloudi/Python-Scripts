import itertools
import urlparse
from webscraping import common, download, xpath

DOMAIN = "www.nytimes.com"
writer = common.UnicodeWriter('articles.csv')

writer.writerow(['Title', 'Num reads', 'URL'])

seen_urls = set() # track which articles URL's already seen, to prevent duplicates

D = download.Download()

# iterate each of the categories
for category_link in ('/developer/knowledge‐base?page=%d', '/developer/articles?page=%d'):
    # iterate the pages of a category
    for page in itertools.count():
        category_html = D.get(urlparse.urljoin(DOMAIN, category_link % page))
        article_links = xpath.search(category_html, '//div[@class="morelink"]/a/@href')
        num_new_articles = 0
        for article_link in article_links:
            # scrape each article
            url = urlparse.urljoin(DOMAIN, article_link)
            if url not in seen_urls:
                num_new_articles += 1
                seen_urls.add(url)
                html = D.get(url)
                title = xpath.get(html, '//div[@class="feed‐header‐wrap"]/h2')
                num_reads = xpath.get(html, '//li[@class="statistics_counter last"]/span').replace
                row = title, num_reads, url
                writer.writerow(row)
        if num_new_articles == 0:
            break # have found all articles for this category
