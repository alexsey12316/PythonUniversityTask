def custom_input():
    try:
        print('Введите число')
        a = eval(input())
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


print('Простое' if is_prime(custom_input()) else 'Составное')
