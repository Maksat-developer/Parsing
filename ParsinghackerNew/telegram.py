import telebot
from telebot import types

bot = telebot.TeleBot('')
#  qwer это старт бота
@bot.message_handler(commands=['start'])
def welcom(message): # создаем функцию которая приветствует пользователя при нажатии старта

    photo = open('') # перердаем с помошью функции "open" картинку в формате "jpeg"

    bot.send_photo(message.chat.id, photo) # тут предаем message-в чат телеграмма photo это переменная

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1. переменная markup.
                                                             # 2.types указывем тип кнопок
                                                             # 3.ReplyKeyboardMarkup
                                                             # 4.resize_keyboard=True пускай выводит мне следуюшие кнопки

    button1 = types.KeyboardButton('Могу приступить к осмотру моделей') # первая созданная кнопка которая высвечивает
                                                   # сообщение 'Идем дальше'
    bot.send_message(message.chat.id,
                     f' "#" {message.from_user}',
                     reply_markup=markup)

    button2 = types.KeyboardButton('"Купить смартфон"') # тут добавляем кнопку еше одну с помошью переменной 'button2'
                                                # и передаем ей тип кнопки 'types'-'KeyboardButton'

    markup.add(button1,button2) # в переменну 'markup' мы добавляем
                                # эти две переменные в которых есть кнопки "button1", "button2"
# создаем декоратор в которую заварачиваем новые кнопки и действия к ним
@bot.message_handler(content_types = ['text']) # Декоратор
def aswer(message): # функция отвечать на конпки

    if message.text == "#":  # если нажать на кнопку  " # "
        bot.send_message(message.chat.id, '#') # то выведи мне следующее сообщение
    elif message.text == '#': # а еше если нажмет на кнопку " # " то выведи следующие типы марок смартфона

        markup = types.InlineKeyboardMarkup(row_width=3) # в начале обозначаете тип кнопок для следующих марок смартфона

        button3= types.InlineKeyboardButton("iphone", # создаёте переменную
                                                      # в которую указвается тип кнопки и "имя кнопки"
                                                      # дальще callback_data="имя кнопки "
                                            callback_data='iphone')

        button4 = types.InlineKeyboardButton("iphone 2",
                                             callback_data='iphone 2')

        button5 = types.InlineKeyboardButton("iphone 3",
                                             callback_data='iphone 3')

        markup.add(button3,button4,button5) # обьединяете все кнопки с помощью метода .add()
                                            # добавляете в ранее созданном переменном (markup) где указан тип кнопки

        bot.send_message(message.chat.id, # вместе с кнопками высветилась сообщение
                                          # передаёте ее в bot.send_message(message.chat.id, " # ", reply_markup=markup)
                         'Какую марку айфона вы хотите?',
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'error') # в другом случае показывай сообщение "error"

@bot.callback_query_handler(func=lambda call : True) # заварачиваем это все в декоратор в котором
def callback_inline(call): # создаем новую функцию которая отвечает за обратный вызов то есть ответ на кнопки
    try: # Засовываем это все в проверку
        if call.message: # если " call " это message то
            if call.data == 'iphone':  # и если нажали на кнопку " iphone "
                bot.send_message(call.message.chat.id, #  то высвети следующее сообщение
                                 '500$')

            if call.data == 'iphone 2':
                bot.send_message(call.message.chat.id,
                                     '600$')

            if call.data == 'iphone 3':
                bot.send_message(call.message.chat.id,
                                     '700$')

    except:
        print('error')

bot.polling(none_stop=True)