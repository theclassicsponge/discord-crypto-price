from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    achethree = soup.find_all('h3')
    for aches in achethree:
        print(aches.text)
