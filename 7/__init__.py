from math import sqrt

t = 0
while t != 1 and t != 2:
    t = int(input('Нажмите '
                  '"1" для ввода параметров треугольника через длины сторон  '
                  '"2" - ввод параметров через координаты вершин \n'))

if t == 1:
    def custom_input():
        try:
            print('Введите a,b,c каждое число в новой строке')
            a = eval(input())
            b = eval(input())
            c = eval(input())
            if a <= 0 or b <= 0 or c <= 0:
                raise Exception
            return a, b, c
        except:
            print('Попробуйте снова')
            return custom_input()


    a, b, c = custom_input()

    p = (a + b + c) / 2
    print(f'Площадь равна {sqrt(p * (p - a) * (p - b) * (p - c))}')


else:
    def custom_input():
        try:
            print('Введите координаты каждая пара в новой строке')
            x1, y1 = map(eval, input().split(' '))
            x2, y2 = map(eval, input().split(' '))
            x3, y3 = map(eval, input().split(' '))

            return x1, y1, x2, y2, x3, y3
        except:
            print('Попробуйте снова')
            return custom_input()


    x1, y1, x2, y2, x3, y3 = custom_input()
    print(f'Площадь равна {abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2}')
