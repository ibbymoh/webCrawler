from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):
    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    #We will call the HTML parser function feed on some set of HTML and this function will be called to handle the start tags
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == 'a':
            for (attribute,value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url,value)
                    self.links.add(url)

    def page_links(self):
        #returns all of our links
        return self.links

    def error(self, message: str):
        pass