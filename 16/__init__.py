import re


def custom_input():
    try:
        print('Введите число')
        a = int(input())
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


n = custom_input()
pattern = '^a[a-z]\d{2}55661$'
res_list = []
list_of_str = input('Введите билеты\n').split(' ')
for i in list_of_str:
    if re.match(pattern, i):
        res_list.append(i)

if len(res_list) == 0:
    print(-1)
else:
    print(' '.join(res_list))

