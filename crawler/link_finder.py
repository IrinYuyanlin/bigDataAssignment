from HTMLParser import *
import urlparse
import urllib


class linkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        HTMLParser.__init__(self)
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def page_links(self):
        return self.links

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = urlparse.urljoin(self.base_url, value)
                    self.links.add(url)
