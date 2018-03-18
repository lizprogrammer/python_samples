from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><p>This is <b>invalid HTML</p></html>", "html.parser")

soup = BeautifulSoup("<html><p>This is <b>invalid HTML</p></html>", "html.parser")
print(soup)
# <html><p>This is <b>invalid HTML</b></p></html>

soup = BeautifulSoup("html.parser", "lxml")
print(soup)
# <html><body><p>This is <b>invalid HTML</b></p></body></html>

soup = BeautifulSoup("<html><p>This is <b>invalid HTML</p></html>", "xml")
print(soup)
# <?xml version="1.0" encoding="utf-8"?>
# <html><p>This is <b>invalid HTML</b></p></html>

soup = BeautifulSoup("<html><p>This is <b>invalid HTML</p></html>", "html5lib")
print(soup)
# <html><head></head><body><p>This is <b>invalid HTML</b></p></body></html>