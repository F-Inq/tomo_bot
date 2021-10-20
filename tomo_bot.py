from datetime import timezone, timedelta, datetime
from time import sleep
import telebot
from telebot import types

from weeks_schedule import weeks, bot_token, my_id

bot = telebot.TeleBot(bot_token)

timezone = timezone(timedelta(hours=+3))
print(str(datetime.now(timezone))[:-13] + ' // Bot online')
bot.send_message(my_id, str(datetime.now())[:-7] + ' // Bot online')  # PM to me that bot is now working

start_help = (
    'Напиши "Расписание", чтобы узнать расписание на текущую или следующую неделю;\n\
    \n\
    Напиши номер недели, чтобы узнать на неё расписание.'
)


@bot.message_handler(commands=['start', 'help'])
def start_command(message):
    bot.send_message(message.chat.id, start_help)


laugh = {'х', 'а', 'a', 'h', 'x', ')', 'п', 'в', 'з'}
not_laugh = {'папаха', 'запах', 'ваза', 'ваха', 'ахав'}


def detect_laugh(string):
    for word in string.split():
        if (not any(x in word for x in not_laugh)
                and laugh.issuperset(set(word)) and len(word) > 3 and len(set(word)) > 1):
            return True


def detect_bot(string):
    for word in string.split():
        if word == 'bot' or word == 'бот':
            return True


schedule = {'расписание', 'hfcgbcfybt', 'raspisanie', 'schedule'}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    inp = message.text.lower()
    if inp.isdigit():
        inp = int(inp)
        if 0 < inp < 18:
            bot.send_message(message.chat.id, weeks[inp-1])
            bot.send_message(my_id, 'Someone requested schedule for week ' + str(inp))
    elif inp in schedule:
        keyboard = types.InlineKeyboardMarkup()
        key_this = types.InlineKeyboardButton(text='Эта неделя', callback_data='this')
        keyboard.add(key_this)
        key_next = types.InlineKeyboardButton(text='Следующая неделя', callback_data='next')
        keyboard.add(key_next)
        question = 'Узнать расписание:'
        bot.send_message(message.chat.id, text=question, reply_markup=keyboard)
    else:
        if detect_laugh(inp):
            bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEC3eFhN0_0gRR60XbapUVYGCjyZIj2OwACKAADFXbpBw_Cg-Mb1wfqIAQ')
        if detect_bot(inp):
            bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEC3eNhN1AmPxaFK0d46njtyDZnlKdbfQACUQADFXbpB-KSS5LVyjJ_IAQ')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    d = (datetime.now() - datetime(2021, 8, 30)).days // 7  # Current week number check
    if call.data == 'this':
        bot.send_message(call.message.chat.id, weeks[d])
    elif call.data == 'next':
        bot.send_message(call.message.chat.id, weeks[d + 1])
    bot.send_message(my_id, 'Someone requested schedule for ' + call.data + ' week')


while True:
    try:
        bot.polling(none_stop=True, interval=3)
    except Exception as e:
        print(e)
        sleep(3)
        print(str(datetime.now(timezone))[:-13] + ' // Bot online')
