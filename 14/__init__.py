def custom_input():
    try:
        print('Введите число')
        a = int(input())
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


n = custom_input()
x = 0
while 2 ** x <= n:
    x += 1

print(x)