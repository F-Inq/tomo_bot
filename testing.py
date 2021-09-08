import datetime

timezone = datetime.timezone(datetime.timedelta(hours=+3))
print(str(datetime.datetime.now(timezone))[:-13] + ' // Bot online')
