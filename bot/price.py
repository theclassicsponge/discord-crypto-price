from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = ""

# opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
page_soup.h1
