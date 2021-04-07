def custom_input():
    try:
        x, v, t = map(eval, input('Введите x0, v0, t через пробел\n').split(' '))
        return x, v, t
    except:
        print('Попробуйте снова')
        custom_input()


x, v, t = custom_input()
g = 9.8
print(f'Ответ {x+v*t-g*t**2/2}')
