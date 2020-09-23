import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, url):
        self.url = url

    def retrieve_index_items(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, 'html.parser')
        print(soup.prettify())
