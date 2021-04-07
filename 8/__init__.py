import re


def custom_input():
    in_str = input(
        'В одной строке, через пробел вводятся: вещественное число, '
        'затем символ - знак операции и вещественное число\n')
    if re.match('^\d+(?:\.\d+)?\s[-+*/]\s\d+(?:\.\d+)?$', in_str):
        return in_str.split(' ')
    else:
        print('Попробуйте ещё раз')
        return custom_input()


arr = custom_input()
arr[0] = eval(arr[0])
arr[2] = eval(arr[2])

if arr[1] == '+':
    print(f'{arr[0]} + {arr[2]} = {arr[0] + arr[2]}')
elif arr[1] == '-':
    print(f'{arr[0]} - {arr[2]} = {arr[0] - arr[2]}')
elif arr[1] == '*':
    print(f'{arr[0]} * {arr[2]} = {arr[0] * arr[2]}')
elif arr[1] == '/':
    try:
        print(f'{arr[0]} / {arr[2]} = {arr[0] / arr[2] }')
    except ZeroDivisionError:
        print('Деление на 0')
