laugh = {'х', 'а', 'a', 'h', 'x', ')', 'п', 'в', 'з'}
inp = 'ахахах хахаха ваза азазазх хах)))))) ваз) ваза) ва))) ахуел'

for word in inp.split():
    if 'папаха' not in word and 'запах' not in word and 'ваза' not in word:
        if laugh.issuperset(set(word)) and len(word) > 3 and len(set(word)) > 1:
            print(word + ' - is laugh')

