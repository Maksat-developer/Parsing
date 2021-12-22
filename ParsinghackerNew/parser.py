import requests #
from bs4 import BeautifulSoup
import csv
# from pprint import pprint as pp
CSV= 'sulpak_smartphones.csv'
HOST = 'https://www.sulpak.kg'
URL = 'https://www.sulpak.kg/f/smartfoniy'
#
HEADERS = {  #
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                   ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.3'

}
def get_html(url, params=''):
    getzapros = requests.get(URL,headers = HEADERS,params = params, verify = False)
    return getzapros

# print(getzapros)

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser') #
    items = soup.findAll('div', class_= 'goods-tiles') #
# print(items) #
    l = []
    for item in items:  #
        l.append({
            'Название': item.find('h3', class_= 'title').get_text(strip=True),
            'Цена' : item.find('div', class_='price').get_text(strip=True),
            'Фото' : item.find('div', class_='goods-photo').find('a').find('img').get('src'),
            'Ссылка на товар' : HOST + item.find('div', class_='product-container-right-side').find('a').get('href'),

    })
# pp(l)
    return l

def save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([ 'Название', 'Цена', 'Фото', 'Ссылка на товар' ])
        for item in items:
            writer.writerow([item['Название'],
                             item['Цена'],
                             item['Фото'],
                             item['Ссылка на товар']])

def pogination():
    PAGENATION = input('Введите количество страниц')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        list_page = []
        for page in range(1, PAGENATION):
            print(f'Страница {page} готова')
            html = get_html(URL, params={'page': page})
            list_page.extend(get_content(html.text))
        save(list_page, CSV)
        print('Парсинг готов')
    else:
        print('error')

pogination()










