def custom_input():
    try:
        print('Введите a,b каждое число в новой строке')
        a = eval(input())
        b = eval(input())
        return a, b
    except:
        print('Попробуйте снова')
        return custom_input()


def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        res = a
        for i in range(1, b):
            res *= a
        return res
    else:
        return 1 / pow(a, -1 * b)


a, b = custom_input()

print(pow(a, b))
