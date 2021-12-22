import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

URL = 'https://www.kivano.kg/mobilnye-telefony'
HOST = 'https://www.kivano.kg'
HEADERS = {
 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'

}

r = requests.get(URL, headers=HEADERS, verify=False)
#print(r)
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)
items = soup.findAll('div', class_='item product_listbox oh')
#print(items)

l = []
for item in items:
 l.append({
  "Название:": item.find('div', class_='listbox_title oh').get_text(strip=True),
  "Цена": item.find('div', class_='listbox_price text-center').get_text(strip=True),
  "Фото": HOST + item.find('div', class_='listbox_img pull-left').find('img').get('src'),
  "Ссылка на товар": HOST + item.find('div', class_='listbox_title oh').find('a').get('href')
 })

pp(l)