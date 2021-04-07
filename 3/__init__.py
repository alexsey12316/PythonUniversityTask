a = eval(input('Введите первый аргумент\n'))
b = eval(input('Введите второй аргумент\n'))

print(f'{a}+{b} = {a+b}')
print(f'{a}-{b} = {a-b}')
print(f'{a}*{b} = {a*b}')
print(f'{a}/{b} = { a/b if b!=0  else "деление на ноль" }')
