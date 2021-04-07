from random import random


def custom_input():
    try:
        print('Введите число')
        a = int(input())
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


while True:
    secret = int(random() * 100)
    flag = True
    for i in range(0, 4):
        attempt = custom_input()
        if attempt == secret:
            print('Поздравляю! Вы угадали')
            flag = False
            break
        elif attempt < secret:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')

    if flag:
        print(f'Вы проиграли. Было загадано: {secret}')
    if input('Желаете попробывать ещё раз? (Введите 1)') != '1':
        break
