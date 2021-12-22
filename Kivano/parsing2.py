import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

HOST = 'https://www.kivano.kg'

URL = 'https://www.kivano.kg/mobilnye-telefony'

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'

}
def get_html(url,params=''):
    zapros = requests.get(URL,headers = HEADERS, params = params, verify = False),
    return zapros



def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_='item product_listbox oh')
    # print(items)

    list = []
    for item in items:
        list.append({
            'Название': item.find('div', class_='listbox_title oh').get_text(strip=True),
            'Цена': item.find('div', class_='listbox_price text-center').get_text(strip=True),
            'Фото': item.find('div', class_='product_img pull-left').find('a').find('img').get('src'),
            'Ссылка на товар': HOST + item.find('div', class_='listbox_title oh').find('img').get('src')

    })
    pp(list)
    return list

