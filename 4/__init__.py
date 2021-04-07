a = eval(input('Введите первый аргумент\n'))
b = eval(input('Введите второй аргумент\n'))

print(f'Вы ввели a = {a}, b = {b}')
c = a
a = b
b = c
print(f'Обмен a = {a}, b = {b}')

a -= b
b += a
a = b - a

print(f'Обмен a = {a}, b = {b}')

