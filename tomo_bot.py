import configparser
from telebot import telebot, types
from datetime import timezone, timedelta, datetime
from string import punctuation

from private_info import bot_token, my_id, professors

bot = telebot.TeleBot(bot_token)

timezone = timezone(timedelta(hours=+3))
print(f'{str(datetime.now(timezone))[:-13]} // Bot online')
bot.send_message(my_id, f'{str(datetime.now())[:-7]} // Bot online')  # PM to me that bot is now working

start_help = ('Напиши "Расписание", чтобы узнать расписание на текущую или следующую неделю;\n\
\n\
Напиши номер недели, чтобы узнать на неё расписание.'
              )

laugh = {'х', 'а', 'a', 'h', 'x', 'п', 'в', 'з'}
not_laugh = {'папаха', 'папах', 'запах', 'запаха', 'заппа', 'ахав', 'ваза', 'ваха', 'папа'}
schedule = {'расписание', 'hfcgbcfybt', 'raspisanie', 'schedule'}
session = {'сессия', 'ctccbz', 'sessiya', 'session'}
config = configparser.ConfigParser()


def strip_punctuation(string):  # removes all the punctuation from incoming message
    for char in string:
        if char in punctuation:
            string = string.replace(char, '')
    return string


def detect_laugh(string):  # returns true if there is laugh in the incoming message
    for word in string.split():
        if (word not in not_laugh
                and laugh.issuperset(set(word))  # word consists only of characters in {laugh}
                and len(word) > 3  # ha and hah are okay
                and len(set(word)) > 1):  # hhh / aaaa is not laugh
            return True


def detect_bot(string):  # returns true if at least one of the words in the message is bot/бот
    for word in string.split():
        if word == 'bot' or word == 'бот':
            return True


def week_schedule(week_n):  # returns a schedule for a week number week_n
    config.read('schedule.ini', encoding="utf-8")
    out = []
    for day, day_schedule in config.items(str(week_n)):
        if day_schedule:
            out.append(day_schedule)
    return out


def get_professor(name):  # works only for session week, returns all the exams with the said professor
    config.read('schedule.ini', encoding="utf-8")
    out = []
    for day, day_schedule in config.items('session'):
        if name in day_schedule:
            out.append(day_schedule)
    return out


def send_schedule(chat, week_index):  # sends a message for each day in schedule for desired week
    d = (datetime.now() - datetime(2021, 8, 30)).days // 7  # Current week number check

    if week_index == 'this':  # conversion from call.data to integer index for current and next weeks
        week_index = d + 1
    elif week_index == 'next':
        week_index = d + 2

    for study_day in week_schedule(week_index):
        bot.send_message(chat, study_day)


@bot.message_handler(commands=['start', 'help'])  # start/help commands handler
def start_command(message):
    bot.send_message(message.chat.id, start_help)


@bot.message_handler(content_types=['text'])  # main message handler
def get_text_messages(message):
    inp = strip_punctuation(message.text.lower())
    if message.text == '/edit':  # doesn't work as a command for some reason
        ans = bot.send_message(message.chat.id, 'Week number?')
        bot.register_next_step_handler(ans, edit_week)  # launches edit_week(ans)
    elif inp.isdigit():
        inp = int(inp)
        if 0 < inp < 18:
            send_schedule(message.chat.id, inp)
            bot.send_message(my_id, f'Someone requested schedule for week {str(inp)}')
    elif inp.title() in professors:  # checks if said professor's exams are needed
        for exam in get_professor(inp.title()):
            bot.send_message(message.chat.id, exam)
    elif inp in session:
        send_schedule(message.chat.id, 'session')
    elif inp in schedule:  # creates a keyboard with 'this-', 'next week schedule' and 'session' buttons
        keyboard = types.InlineKeyboardMarkup()
        key_this = types.InlineKeyboardButton(text='Эта неделя', callback_data='this')
        keyboard.add(key_this)
        key_next = types.InlineKeyboardButton(text='Следующая неделя', callback_data='next')
        keyboard.add(key_next)
        key_sess = types.InlineKeyboardButton(text='Сессия', callback_data='session')
        keyboard.add(key_sess)
        question = 'Узнать расписание:'
        bot.send_message(message.chat.id, text=question, reply_markup=keyboard)
    else:
        if detect_laugh(inp):
            bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEC3eFhN0_0gRR60XbapUVYGCjyZIj2OwACKAADFXbpBw_Cg-Mb1wfqIAQ')
        if detect_bot(inp):
            bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEC3eNhN1AmPxaFK0d46njtyDZnlKdbfQACUQADFXbpB-KSS5LVyjJ_IAQ')


@bot.callback_query_handler(func=lambda call: True)  # schedule keyboard button push handling
def callback_worker(call):
    send_schedule(call.message.chat.id, call.data)
    bot.send_message(my_id, f'Someone requested schedule for {call.data} week')


########################################################################################################################
"""
Editing schedule with the bot
"""
edit_info = {'week': '0', 'day': 'hed'}
allowed_days = ('hed', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat')


def edit_week(message):
    global edit_info
    try:
        edited_week = int(message.text)
        if 0 < edited_week < 18:
            edit_info['week'] = str(edited_week)
            ans = bot.send_message(message.chat.id, 'Day?')
            bot.register_next_step_handler(ans, edit_day)
        else:
            bot.send_message(message.chat.id, 'Edit cancelled')
    except ValueError:
        bot.send_message(message.chat.id, 'Edit cancelled')


def edit_day(message):
    global edit_info
    edited_day = str(message.text.lower())
    if edited_day in allowed_days:
        edit_info['day'] = edited_day
        config.read('schedule.ini', encoding="utf-8")
        bot.send_message(message.chat.id, config[edit_info['week']][edit_info['day']])
        ans = bot.send_message(message.chat.id, '\nPlease send new schedule:')
        bot.register_next_step_handler(ans, edit_schedule)
    else:
        bot.send_message(message.chat.id, 'Edit cancelled')


def edit_schedule(message):
    global edit_info
    if message.text.lower() == 'stop' or message.text.lower() == 'стоп':
        bot.send_message(message.chat.id, 'Edit cancelled')
    else:
        config[edit_info['week']][edit_info['day']] = message.text
        with open('schedule.ini', 'w', encoding="utf-8") as configfile:
            config.write(configfile)
        bot.send_message(message.chat.id, f'Edit done.\n'
                                          f'New schedule for week {edit_info["week"]}:')
        bot.send_message(message.chat.id, f'{week_schedule(int(edit_info["week"]))}')


while True:
    try:
        bot.polling(none_stop=True, interval=2)
    except Exception as e:
        print(e)
        print(f'{str(datetime.now(timezone))[:-13]} // Exception\n'
              f'\n'
              f'{str(datetime.now(timezone))[:-13]} // Bot online')
