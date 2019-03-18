#http://searchcode.com/codesearch/view/64187115/
#!/usr/bin/env python

from collections import deque
import httplib
from HTMLParser import HTMLParser
import logging
import optparse
import sys
import urllib
import urlparse

class LinkExtractorParser(HTMLParser):
    """
    An implementation of the HTML parser that detects links and collects the
    href URL's.
    """
    def __init__(self, base_url):
        HTMLParser.__init__(self)
        self.accepted_schemes = set(['file', 'http', 'https'])
        self.base_url = base_url
        self.outgoing_links = set()

    def handle_starttag(self, tag, attributes):
        """
        Processes an opening HTML tag. Collects link URL's from 'a' nodes.
        """
        HTMLParser.handle_starttag(self, tag, attributes)
        if tag == 'a':
            for (name, value) in attributes:
                if name == 'href':
                    self.add_outgoing_link(value)

    # TODO: extract text from the document

    def add_outgoing_link(self, href):
        """
        Adds a link to the list of ongoing links in the document.
        """
        # Convert the link to absolute URL.
        url = urlparse.urljoin(self.base_url, href)
        # Remove fragment from the URL so that the page is not downloaded
        # again for other fragments.
        (url, fragment) = urlparse.urldefrag(url)
        parsed_url = urlparse.urlparse(url)
        if parsed_url.scheme in self.accepted_schemes:
            self.outgoing_links.add(url)

class Downloader:
    """The downloader for the crawler."""

    def __init__(self, seed_url, max_depth, search_phrase, url_filter, verbose = False):
        self.max_depth = max_depth
        self.seed_url = seed_url
        self.visited_urls = dict()
        self.processing_queue = deque([(seed_url, 0)])
        self.queued_documents = set([seed_url])
        self.search_phrase = search_phrase
        self.matching_documents = list()
        self.url_filter = url_filter
        self.blacklisted_urls = set()

    def process_urls(self, max_pages = None):
        processed_pages = 0
        while len(self.processing_queue) > 0:
            if max_pages == 0:
                return processed_pages
            (url, level) = self.dequeue_url()
            if self.process_single_url(url, level):
                if max_pages is not None and max_pages > 0:
                    max_pages -= 1
                processed_pages += 1
        return processed_pages

    def process_single_url(self, url, level):
        """
        Downloads the contents from the given url and parses it as a HTML
        document and detects links to further documents.

        Returns True if a new page was processed; otherwise, returns False.
        """
        logging.info("Processing URL %s", url)
        # The contents fetched from the URL
        contents = None
        # Information about the data returned by the URL. Used for filtering
        # by mime type.
        mime_info = None
        final_url = None
        # Download the contents of the URL
        try:
            logging.debug("Downloading contents...")
            contents_handle = urllib.urlopen(url)
            mime_info = contents_handle.info()
            # TODO: Add allowed mime-types as a parameter of the crawler
            mime_type = mime_info.gettype()
            if mime_type != 'text/html':
                logging.info("Unsupported mime type: %s", mime_type)
                contents_handle.close()
                return False
            contents = contents_handle.read()
            final_url = contents_handle.geturl()
            logging.info("Final URL: %s", final_url)

            # TODO: detection of <meta> redirects

            contents_handle.close()
            logging.debug("Download complete")

            # Mark the document as processed; add both the request URL, and the
            # URL from which the document was finally returned (accounting for
            # redirects).
            def set_depth(collection, link, level):
                """
                Set collection[link] to level; keep the current value if it is
                lower than level.
                """
                if link in collection:
                    level = min(collection[link], level)
                collection[link] = level
            set_depth(self.visited_urls, url, level)
            set_depth(self.visited_urls, final_url, level)

            # Parse the HTML document (hope it is a HTML document)
            link_extractor = LinkExtractorParser(final_url)
            link_extractor.feed(contents)

            if level < self.max_depth:
                self.add_outgoing_links(link_extractor.outgoing_links,
                                        level + 1)
            
            # Search the document (including the markup) for the search phrase.
            # TODO: do not search markup and comments
            if contents.find(self.search_phrase) < 0:
                return True
            if self.url_filter is not None:
                if url.find(self.url_filter) < 0:
                    return True
                if final_url.find(self.url_filter) < 0:
                    return True
            self.matching_documents.append(final_url)
            return True
        except BaseException as err:
            logging.warning("Processing of %s failed", str(url))
            return False

    def add_outgoing_links(self, links, level):
        for link in links:
            if (link not in self.visited_urls and
                link not in self.queued_documents):
                self.enqueue_url(link, level)

    def dequeue_url(self):
        (link, level) = self.processing_queue.popleft()
        self.queued_documents.remove(link)
        print "Processing: ", link
        return (link, level)

    def enqueue_url(self, link, level):
        self.processing_queue.append((link, level))
        self.queued_documents.add(link)

    def print_matching_urls(self):
        for url in self.matching_documents:
            if url in self.blacklisted_urls:
                print "BLACK", url
            print url

def parse_options(argv):
    """
    Parses command-line options from argv. Returns an object that contains the
    values of the options. The object contains at least the following
    attributes:
    - max_depth is the maximal depth used by the crawler,
    - max_pages is the maximal number of pages downloaded by the crawler,
    - search_phrase is the search phrase,
    - seed_url is the seed url for the parser,
    - url_filter is the substring that must be in the URL for the document to
      match
    """
    # TODO: Write the help strings.
    parser = optparse.OptionParser()
    parser.add_option('-d', '--max_depth',
                      action='store', dest='max_depth', type='int',
                      default='3',
                      help='The maximal depth (number of links between the '\
                           'seed URL and the downloaded page) allowed by the '\
                           'crawler.')
    parser.add_option('-m', '--max_pages',
                      action='store', dest='max_pages', type='long',
                      default=None,
                      help='The maximal number of pages downloaded by the '\
                           'crawler. If not specified, there is no limit on '\
                           'the number of pages.')
    parser.add_option('-s', '--search_phrase',
                      action='store', dest='search_phrase', type='string',
                      help='The phrase to search for in the downloaded pages. '\
                           'This is a mandatory argument.')
    parser.add_option('-u', '--seed_url',
                      action='store', dest='seed_url', type='string',
                      help='The seed URL for the crawler. This is a mandatory '\
                           'argument.')
    parser.add_option('-f', '--url_filter',
                      action='store', dest='url_filter', type='string',
                      default = None,
                      help='A filter for the URL\'s of matching documents.')
    (options, args) = parser.parse_args(argv)
    if options.seed_url is None or options.search_phrase is None:
        parser.print_help()
        return None
    return options

if __name__ == '__main__':
    logging.basicConfig()
    options = parse_options(sys.argv)
    if options is None:
        sys.exit(1)
    downloader = Downloader(options.seed_url,
                            options.max_depth,
                            options.search_phrase,
                            options.url_filter)
    downloader.print_matching_urls()
