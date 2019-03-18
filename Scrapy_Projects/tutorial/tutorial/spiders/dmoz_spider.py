import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.nytimes.com/pages/technology",
        "http://www.nytimes.com/pages/science"
        ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename + ".txt", 'wb') as f:
            f.write(response.body)
            
