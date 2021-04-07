import itertools
import re


def custom_input():
    try:
        a = int(input())
        if not 1 <= a <= 8:
            raise Exception
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


def custom_str_input():
    try:
        a = input()
        if not re.match('^[a-z]{1,8}$', a):
            raise Exception
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


print('Введите n')
n = custom_input()
print('Введите строку')
word = custom_str_input()

for i in itertools.product(word, repeat=n):
    res = ''.join(i)
    isContains = True
    for j in word:
        if not res.__contains__(j):
            isContains = False
    if isContains:
        print(res, end=' ')
