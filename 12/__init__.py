def custom_input():
    try:
        print('Введите число')
        a = eval(input())
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


def fact(a):
    if a <= 1:
        return 1
    return fact(a - 1) * a

print(fact(custom_input()))
