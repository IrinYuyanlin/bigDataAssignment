from HTMLParser import *
from urllib import *


class linkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def page_links(self):
        return self.links

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        print(tag)
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = urllib.urljoin(self.base_url, value)
                    self.links.add(url)