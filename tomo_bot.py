import datetime
import time
import telebot
from telebot import types

bot_token = '1774674419:AAGs90j0GONVGOMG2IxK81bSVIrJ6jA3DFo'

# Расписание по неделям

w1 = ('Неделя №1\n\
30.08 - 05.09\n\
\n\
Занятий нет'
      )

w2 = ('Неделя №2\n\
06.09 - 12.09\n\
\n\
Вторник:\n\
12:40 - 14:10 // Физические принципы микро и оптоэлектроники (Д)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика (Д)\n\
12:40 - 14:10 // Волоконная оптика (Д)'
      )

w3 = ('Неделя №3\n\
13.09 - 19.09\n\
\n\
Вторник:\n\
14:20 - 15:50 // Технологии роста и обработки кристаллов (Д)\n\
16:20 - 17:50 // Физические принципы микро и оптоэлектроники (каб. 200)\n\
18:00 - 19:30 // Физические принципы микро и оптоэлектроники (каб. 200)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (Д)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика (каб. 200)\n\
12:40 - 14:10 // Волоконная оптика (каб. 200)'
      )

w4 = ('Неделя №4\n\
20.09 - 26.09\n\
\n\
Вторник:\n\
12:40 - 14:10 // Физические принципы микро и оптоэлектроники (Д)\n\
\n\
Среда:\n\
16:20 - 17:50 // Технологии роста и обработки кристаллов (каб. 200)\n\
18:00 - 19:30 // Технологии роста и обработки кристаллов (каб. 200)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (каб. 208)\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (каб. 208)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика (Д)\n\
12:40 - 14:10 // Волоконная оптика (Д)'
      )

w5 = ('Неделя №5\n\
27.09 - 03.10\n\
\n\
Вторник:\n\
16:20 - 17:50 // Физические принципы микро и оптоэлектроники (каб. 200)\n\
18:00 - 19:30 // Физические принципы микро и оптоэлектроники (каб. 200)\n\
\n\
Среда:\n\
14:20 - 15:50 // Технологии роста и обработки кристаллов (Д)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (Д)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика (каб. 200)\n\
12:40 - 14:10 // Волоконная оптика (каб. 200)'
      )

w6 = ('Неделя №6\n\
04.10 - 10.10\n\
\n\
Вторник:\n\
12:40 - 14:10 // Физические принципы микро и оптоэлектроники (Д)\n\
\n\
Среда:\n\
16:20 - 17:50 // Технологии роста и обработки кристаллов (каб. 200)\n\
18:00 - 19:30 // Технологии роста и обработки кристаллов (каб. 200)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (каб. 208)\n\
14:20 - 15:50 // Технологии разработки оптоэлектронных систем (каб. 208)'
      )

w7 = ('Неделя №7\n\
11.10 - 17.10\n\
\n\
Вторник:\n\
16:20 - 17:50 // Физические принципы микро и оптоэлектроники ЛАБА  (каб. 204)\n\
18:00 - 19:30 // Физические принципы микро и оптоэлектроники ЛАБА  (каб. 204)\n\
\n\
Среда:\n\
14:20 - 15:50 // Технологии роста и обработки кристаллов (Д)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (Д)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика (каб. 200)\n\
12:40 - 14:10 // Волоконная оптика (каб. 200)'
      )

w8 = ('Неделя №8\n\
18.10 - 24.10\n\
\n\
Вторник:\n\
12:40 - 14:10 // Физические принципы микро и оптоэлектроники (Д)\n\
\n\
Среда:\n\
16:20 - 17:50 // Технологии роста и обработки кристаллов (каб. 200)\n\
18:00 - 19:30 // Технологии роста и обработки кристаллов (каб. 200)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (каб. 208)\n\
14:20 - 15:50 // Технологии разработки оптоэлектронных систем (каб. 208)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика ЛАБА  (каб. 200)\n\
12:40 - 14:10 // Волоконная оптика ЛАБА  (каб. 200)'
      )

w9 = ('Неделя №9\n\
25.10 - 31.10\n\
\n\
Среда:\n\
14:20 - 15:50 // Технологии роста и обработки кристаллов (Д)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (Д)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика (каб. 200)\n\
12:40 - 14:10 // Волоконная оптика (каб. 200)'
      )

w10 = ('Неделя №10\n\
01.11 - 07.11\n\
\n\
Вторник:\n\
10:40 - 12:10 // Физические принципы микро и оптоэлектроники (Сапфир)\n\
12:40 - 14:10 // Физические принципы микро и оптоэлектроники (Сапфир)\n\
\n\
Среда:\n\
16:20 - 17:50 // Технологии роста и обработки кристаллов (каб. 200)\n\
18:00 - 19:30 // Технологии роста и обработки кристаллов (каб. 200)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (каб. 208)\n\
14:20 - 15:50 // Технологии разработки оптоэлектронных систем (каб. 208)'
       )

w11 = ('Неделя №11\n\
08.11 - 14.11\n\
\n\
Вторник:\n\
16:20 - 17:50 // Физические принципы микро и оптоэлектроники (каб. 200)\n\
18:00 - 19:30 // Физические принципы микро и оптоэлектроники (каб. 200)\n\
\n\
Среда:\n\
16:20 - 17:50 // Технологии роста и обработки кристаллов ЛАБА  (каб. 127)\n\
18:00 - 19:30 // Технологии роста и обработки кристаллов ЛАБА  (каб. 127)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (Д)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика (каб. 200)\n\
12:40 - 14:10 // Волоконная оптика (каб. 200)'
       )

w12 = ('Неделя №12\n\
15.11 - 21.11\n\
\n\
Вторник:\n\
10:40 - 12:10 // Физические принципы микро и оптоэлектроники (Сапфир)\n\
12:40 - 14:10 // Физические принципы микро и оптоэлектроники (Сапфир)\n\
\n\
Среда:\n\
16:20 - 17:50 // Технологии роста и обработки кристаллов (каб. 200)\n\
18:00 - 19:30 // Технологии роста и обработки кристаллов (каб. 200)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (каб. 208)\n\
14:20 - 15:50 // Технологии разработки оптоэлектронных систем (каб. 208)'
       )

w13 = ('Неделя №13\n\
22.11 - 28.11\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (Д)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика (каб. 200)\n\
12:40 - 14:10 // Волоконная оптика (каб. 200)'
       )

w14 = ('Неделя №14\n\
29.11 - 05.12\n\
\n\
Вторник:\n\
10:40 - 12:10 // Физические принципы микро и оптоэлектроники (Сапфир)\n\
12:40 - 14:10 // Физические принципы микро и оптоэлектроники (Сапфир)\n\\n\
\n\
Среда:\n\
16:20 - 17:50 // Технологии роста и обработки кристаллов (каб. 200)\n\
18:00 - 19:30 // Технологии роста и обработки кристаллов (каб. 200)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (каб. 208)\n\
14:20 - 15:50 // Технологии разработки оптоэлектронных систем (каб. 208)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика ЛАБА  (каб. 200)\n\
12:40 - 14:10 // Волоконная оптика ЛАБА  (каб. 200)'
       )

w15 = ('Неделя №15\n\
06.12 - 12.12\n\
\n\
Вторник:\n\
16:20 - 17:50 // Физические принципы микро и оптоэлектроники ЛАБА  (каб. 204)\n\
18:00 - 19:30 // Физические принципы микро и оптоэлектроники ЛАБА  (каб. 204)\n\
\n\
Среда:\n\
16:20 - 17:50 // Технологии роста и обработки кристаллов ЛАБА  (каб. 127)\n\
18:00 - 19:30 // Технологии роста и обработки кристаллов ЛАБА  (каб. 127)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (Д)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика (каб. 200)\n\
12:40 - 14:10 // Волоконная оптика (каб. 200)'
       )

w16 = ('Неделя №16\n\
13.12 - 19.12\n\
\n\
Вторник:\n\
10:40 - 12:10 // Физические принципы микро и оптоэлектроники (Сапфир)\n\
12:40 - 14:10 // Физические принципы микро и оптоэлектроники (Сапфир)\n\
\n\
Среда:\n\
16:20 - 17:50 // Технологии роста и обработки кристаллов (каб. 200)\n\
18:00 - 19:30 // Технологии роста и обработки кристаллов (каб. 200)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (каб. 208)\n\
14:20 - 15:50 // Технологии разработки оптоэлектронных систем (каб. 208)'
       )

w17 = ('Неделя №17\n\
20.12 - 26.12\n\
\n\
Вторник:\n\
16:20 - 17:50 // Физические принципы микро и оптоэлектроники (каб. 200)\n\
18:00 - 19:30 // Физические принципы микро и оптоэлектроники (каб. 200)\n\
\n\
Четверг:\n\
12:40 - 14:10 // Технологии разработки оптоэлектронных систем (Д)\n\
\n\
Суббота:\n\
10:40 - 12:10 // Волоконная оптика (каб. 200)\n\
12:40 - 14:10 // Волоконная оптика (каб. 200)'
       )

weeks = (w1, w2, w3, w4, w5, w6, w7, w8, w9,
         w10, w11, w12, w13, w14, w15, w16, w17)

d = (datetime.datetime.now() - datetime.datetime(2021, 8, 30)).days // 7  # Проверка на номер текущей/следующей недели

start_help = ('Напиши "Расписание", чтобы узнать расписание на текущую или следующую неделю;\
\n\nНапиши номер недели, чтобы узнать на неё расписание.')

schedule = {'расписание', 'hfcgbcfybt', 'raspisanie', 'schedule'}
laugh = {'х', 'а', 'a', 'h', 'x', ')'}

""""
>>>>> САМ БОТ
"""

bot = telebot.TeleBot(bot_token)

timezone = datetime.timezone(datetime.timedelta(hours=+3))
print(str(datetime.datetime.now(timezone))[:-13] + ' // Bot online')
bot.send_message('269854203', str(datetime.datetime.now())[:-7] + ' // Bot online')


@bot.message_handler(commands=['start', 'help'])
def start_command(message):
    bot.send_message(message.chat.id, start_help)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global d
    inp = message.text.lower()
    if inp.isdigit():
        inp = int(inp)
        if 0 < inp < 18:
            bot.send_message(message.chat.id, weeks[inp-1])
            bot.send_message('269854203', 'Someone used the bot')
    else:
        for word in inp.split():
            if 'папаха' not in word and 'запах' not in word and 'ваза' not in word:
                if (laugh.issuperset(word.replace('п', '').replace('в', '').replace('з', ''))
                        and len(word) > 3 and len(set(word)) > 1):
                    bot.send_sticker(message.chat.id,
                                     'CAACAgQAAxkBAAEC3eFhN0_0gRR60XbapUVYGCjyZIj2OwACKAADFXbpBw_Cg-Mb1wfqIAQ')
                    break
            if word == 'bot' or word == 'бот':
                bot.send_sticker(message.chat.id,
                                 'CAACAgQAAxkBAAEC3eNhN1AmPxaFK0d46njtyDZnlKdbfQACUQADFXbpB-KSS5LVyjJ_IAQ')
                break
    if inp in schedule:
        d = (datetime.datetime.now() - datetime.datetime(2021, 8, 30)).days // 7
        keyboard = types.InlineKeyboardMarkup()
        key_this = types.InlineKeyboardButton(text='Эта неделя', callback_data='this')
        keyboard.add(key_this)
        key_next = types.InlineKeyboardButton(text='Следующая неделя', callback_data='next')
        keyboard.add(key_next)
        question = 'Узнать расписание:'
        bot.send_message(message.chat.id, text=question, reply_markup=keyboard)
        bot.send_message('269854203', 'Someone used the bot')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'this':
        bot.send_message(call.message.chat.id, weeks[d])
        bot.send_message('269854203', 'Someone used the bot')
    elif call.data == 'next':
        bot.send_message(call.message.chat.id, weeks[d + 1])
        bot.send_message('269854203', 'Someone used the bot')


while True:
    try:
        bot.polling(none_stop=True, interval=3)
    except Exception as e:
        print(e)
        time.sleep(5)
