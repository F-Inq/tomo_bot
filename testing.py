laugh = {'х', 'а', 'a', 'h', 'x', ')'}
inp = 'ааааааааааааа хахах запах запах) ахах) хуй запахх ваза)))) ваз ахахвхахав ах пхах ахахазхаах хахахахаххзапхз'

for word in inp.split():
    if 'папаха' not in word and 'запах' not in word and 'ваза' not in word:
        if (laugh.issuperset(word.replace('п', '').replace('в', '').replace('з', '')) and
                len(word) > 3 and len(set(word)) > 1):
            print(word + ' - Laugh detected')
