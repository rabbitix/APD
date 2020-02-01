from bs4 import BeautifulSoup
import requests
from time import sleep

def add_to_urls(direct_url):
    with open('urls.txt', 'a') as file:
        file.write(f'{direct_url} \n')


url = input("Paste the url:> ")

page = requests.get(url)
html = page.text

s = BeautifulSoup(html, 'lxml')

playlist = s.find('div', {'class': 'playlist-body'})
all_links = playlist.find_all('a', {'class': 'title'})
links = []
for link in all_links:
    links.append(f"https://www.aparat.com{link.attrs['href']}")

for link in links:
    res = requests.get(link)
    html = res.text
    s = BeautifulSoup(html, 'lxml')
    url = s.select_one('li.link:nth-child(5) > a:nth-child(1)').attrs['href']
    add_to_urls(url)
    