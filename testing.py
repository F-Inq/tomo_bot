laugh = {'х', 'а', 'a', 'h', 'x', ')', 'п', 'в', 'з'}


def detect_laugh(string):
    for word in string.split():
        if 'папаха' not in word and 'запах' not in word and 'ваза' not in word:
            if laugh.issuperset(set(word)) and len(word) > 3 and len(set(word)) > 1:
                return True


def detect_bot(string):
    for word in string.split():
        if word == 'bot' or word == 'бот':
            return True


inp = 'ахахахах ахахах qweqwe бот 1'

if detect_laugh(inp):
    print('laugh detected')
if detect_bot(inp):
    print('yes i am bot')
