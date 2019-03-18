#!/usr/bin/env python
import re
from scrapy.spider import BaseSpider
from scrapy.http import FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib_exp.crawlspider import CrawlSpider, Rule
from scrapy.contrib_exp.crawlspider.reqext import SgmlRequestExtractor
from scrapy.contrib_exp.crawlspider.reqproc import Canonicalize,
FilterDupes
from scrapy.utils.misc import arg_to_iter
import fileinput
from project.settings import CONCURRENT_REQUESTS_PER_SPIDER
from scrapy.http import Request
import os
import time

def get_domains():
    fi = fileinput.FileInput('data.txt')
    for domain in fi:
        domain = 'http://'+domain.rstrip()
        yield domain
    fi.close()

class ScanSpider(BaseSpider):
    name = 'phplinkspider'
    start_urls = get_domains()

    def __init__(self, *a, **kw):

        super(ScanSpider, self).__init__(*a, **kw)
        self.request_extractors = [ SgmlRequestExtractor() ]
        self.request_processors = [ FilterDupes() ]
        self.processed_urls = 0
        self.url_error = 0
        self.url_good = 0
        self.start = time.time()
        self.pid = os.getpid()

    def start_requests(self):

        reqs = []
        for i in xrange(CONCURRENT_REQUESTS_PER_SPIDER):
            url = self.start_urls.next()
            reqs.extend(arg_to_iter(self.make_requests_from_url(url)))
        return reqs

    def parse_error(self,failure):
        #print 'Error encontrado'

        self.processed_urls = self.processed_urls +1
        self.url_error = self.url_error + 1

        yield

Request(self.start_urls.next(),callback=self.parse,errback=self.parse_error)

def parse(self, response):
        self.processed_urls = self.processed_urls +1
        self.url_good = self.url_good + 1

        if 1:
            print '----------------------Spider %d---------------------------' % self.pid
            print 'Processed domains %d - Successfull domains %d -
Failed Domains %d' % (self.processed_urls, self.url_good,
self.url_error)
            delta = time.time() - self.start
            print 'Hecho en %0.3fs' % (delta,)
            print '------------------------------------------------'

        yield
Request(self.start_urls.next(),callback=self.parse,errback=self.parse_error) 
