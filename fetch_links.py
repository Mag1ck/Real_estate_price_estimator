import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?viewType=listing&page=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

temporary = []
output_list = []

def pages():
    a = soup.find_all('li', class_='css-1tospdx')
    for i in a:
        i = int((i.text))
        website_pages = i
        if i > website_pages:
            website_pages = i
    return website_pages

def get_links(soup):
    for i in soup.select('li'):
        for a in i.select('a'):
            temporary.append(a.get('href'))



def filter_links():
    for i in temporary:
        if i.startswith("/pl/oferta/"):
            if i not in output_list:
                output_list.append(i)



def save():
    with open('links.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(output_list)


pages = pages()
for i in range(1, pages):
    url = f'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?viewType=listing&page={i}'
    soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
    get_links(soup)
    filter_links()
    save()
    print(f'Page {i} done')


