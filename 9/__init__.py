import re


def time_input():
    str_input = input()
    if re.match('^([0-1]?[0-9]|2[0-3]):[0-5]?\d$', str_input):
        return map(int, str_input.split(':'))
    else:
        print('Попробуйте ещё раз')
        return time_input()


print('Введите первую дату')
h1, m1 = time_input()
print('Введите вторую дату')
h2, m2 = time_input()

if abs((h1*60+m1)-(h2*60+m2)) > 15:
    print('Встреча не состоится')
else:
    print('Встреча состоится')
