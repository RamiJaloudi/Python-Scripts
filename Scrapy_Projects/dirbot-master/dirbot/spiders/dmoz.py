from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["nytimes.com"]
    start_urls = [
        "http://nytimes.com"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)

        # Original script had the the below line "return items".
        return items
        # However, I included the below item to write to a csv. 
        saveFile = open('crawl_data.txt','w')
        saveFile.write(str(items))
        saveFile.close()

        # Consider adding special features, parse certain items and/or format for db insert.
