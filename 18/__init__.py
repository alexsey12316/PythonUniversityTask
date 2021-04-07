import re

vocabulary = ['hallo', 'klempner', 'das', 'ist', 'fantastisch', 'fluggegecheimen']


def custom_input():
    try:
        print('\nВведите слово')
        a = input()
        if not re.match('^[a-z]+$', a):
            raise Exception
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


word = custom_input()
res = 1.0
for letter in word:
    probability = 0.0
    for w in vocabulary:
        probability += w.count(letter)
    probability /= sum([len(a) for a in vocabulary])
    res *= probability
print(res)
