laugh = {'х', 'а', 'в', 'a', 'h', 'x', ')'}
inp = 'ахахах ахах) хуй ахахвхахав'

if len(inp) > 3:
    for word in inp.split():
        if laugh.issuperset(word) and len(set(word)) > 1:
            print('Laugh detected')
