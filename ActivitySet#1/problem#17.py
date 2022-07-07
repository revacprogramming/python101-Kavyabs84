import re
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup

url=input('\033[1m Enter the Link \033[0m ->')

html_content=urlopen(url)

soup=BeautifulSoup(html_content,"lxml")
all_links=[]
for link  in soup.find_all('a'):
    all_links.append(link.get('href'))
for i in range(7):
    url = Request(all_links[17])
    html_content = urlopen(url)
    soup = BeautifulSoup(html_content,"lxml")
    for title in soup.find_all("title"):
        print(title.get_text())
    all_links.clear() 
    for i in soup.find_all('a'):
        all_links.append(i.get('href'))