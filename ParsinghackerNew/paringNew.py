import requests
from bs4 import BeautifulSoup
import telebot
import json

URL = 'https://news.ycombinator.com/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
bot = telebot.TeleBot('5090981615:AAHPD44nKBiP-klwv78Cj1lVQUQ0IeL7fAE')

@bot.message_handler(commands=['start'])
def parsing(message):

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton("Спарсить сайт")
    item2 = telebot.types.KeyboardButton("Получить ссылки")
    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                    '''Добро пожаловать''',
                    reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    try:
        if message.chat.type == 'private':
            if message.text == "Спарсить сайт":
                r = requests.get(URL, headers=HEADERS, verify=False)
                soup = BeautifulSoup(r.text, 'html.parser')
                news = soup.findAll('a', class_='titlelink')
                news_list = {}
                news_split = URL.split('/')[-1]
                news_split = news_split[:-4]
                for new in news:
                    with open('hacker_news.json', 'a') as f:
                        news_list[news_split] = {
                            'title': new.get_text(strip=True),
                            'link': new.get('href')
                        }
                        json.dump(news_list, f, indent=4, ensure_ascii=False)

                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton("Получить документ",
                                                           callback_data="Получить документ")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 "Парсинг готов",
                                 reply_markup=markup)
            elif message.text == "Получить ссылки":
                with open('hacker_news.json') as file:
                    news_list = json.load(file)
                for k, v in sorted(news_list.items()):
                    news = f"{k['title']} \n {v['link']}"
                bot.send_message(message.chat.id, news)
            else:
                bot.send_message(message.chat.id,
                    "Я не знаю что ответить")
    except:
        print("Что-то не то")
        bot.send_message(message.chat.id, 'Что-то не то')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "Получить документ":
                with open('hacker_news.json') as file:
                    news_list = json.load(file)
                    bot.send_document(call.message.chat.id, news_list)
    except:
        print("Что то не то")
        bot.send_message(call.message.chat.id, "Что то не то")

bot.polling(none_stop=True)


