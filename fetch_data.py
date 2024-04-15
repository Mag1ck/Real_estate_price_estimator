import csv
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

with open('data.csv', 'w', newline='', encoding='utf-8') as file_write:
    writer = csv.writer(file_write)
    writer.writerow(['Link', 'Price', 'Location', 'Area', 'Rooms', 'Floor', 'Rent', 'Building Ownership', 'Construction Status', 'Outdoor', 'Heating', 'Car', 'Description'])

    with open('links.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in row:
                url = f'https://www.otodom.pl{i}'
                soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
                link = url
                try:
                    price = soup.find('strong', class_='css-t3wmkv e1l1avn10').text
                except AttributeError:
                    price = None
                try:
                    location = soup.find('div', class_='css-z9gx1y e3ustps0').text
                except AttributeError:
                    location = None
                try:
                    area = soup.find('div', attrs={'data-testid': 'table-value-area'}).text
                except AttributeError:
                    area = None
                try:
                    rooms = soup.find('div', attrs={'data-testid': 'table-value-rooms_num'}).text
                except AttributeError:
                    rooms = None
                try:
                    floor = soup.find('div', attrs={'data-testid': 'table-value-floor'}).text
                except AttributeError:
                    floor = None
                try:
                    rent = soup.find('div', attrs={'data-testid': 'table-value-rent'}).text
                except AttributeError:
                    rent = None
                try:
                    building_ownership = soup.find('div', attrs={'data-testid': 'table-value-building_ownership'}).text
                except AttributeError:
                    building_ownership = None
                try:
                    construction_status = soup.find('div', attrs={'data-testid': 'table-value-construction_status'}).text
                except AttributeError:
                    construction_status = None
                try:
                    outdoor = soup.find('div', attrs={'data-testid': 'table-value-outdoor'}).text
                except AttributeError:
                    outdoor = None
                try:
                    heating = soup.find('div', attrs={'data-testid': 'table-value-heating'}).text
                except AttributeError:
                    heating = None
                try:
                    car = soup.find('div', attrs={'data-testid': 'table-value-car'}).text
                except AttributeError:
                    car = None
                # try:
                #     description = soup.find('div', class_='css-1wekrze e1lbnp621').text
                # except AttributeError:
                #     description = None
                writer.writerow([link, price, location, area, rooms, floor, rent, building_ownership, construction_status, outdoor, heating, car,
                                 # description
                                 ])
                print(f'{link} number {row.index(i) + 1} done, left {len(row) - row.index(i) - 1}')