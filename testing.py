import datetime

weeks = ('w1', 'w1', 'w3', 'w4', 'w5', 'w6')

delta = (datetime.datetime.now() - datetime.datetime(2021, 8, 30)).days // 7  # Проверка на неделю при вызове расписания

print(weeks[delta])
