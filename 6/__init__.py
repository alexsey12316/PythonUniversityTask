from math import sqrt

def custom_input():
    try:
        print('Введите a,b,c каждое число в новой строке')
        a = eval(input())
        b = eval(input())
        c = eval(input())
        return a, b, c
    except:
        print('Попробуйте снова')
        return custom_input()


a, b, c = custom_input()

if a == 0 and b == 0 and c == 0:
    print("x ∈ (-∞ ; + ∞)")
elif a == 0 and b == 0:
    print('Нет решений')
elif (a == 0 or b == 0) and c == 0:
    print('x = 0')
elif a == 0:
    print(f'x = {b / -c}')
elif b == 0:
    t = -c / a
    if t < 0:
        print('Нет действительных решений')
    else:
        print(f'x = {sqrt(-c / a)}')
elif c == 0:
    print(f'x1 = 0; x2 = {-b / a}')
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        print(f'x1 = {(-b + sqrt(d)) / (2 * a)}; x2 = {(-b - sqrt(d)) / (2 * a)}')
    else:
        print('Нет действительных решений')
