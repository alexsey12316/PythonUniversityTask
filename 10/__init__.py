def custom_input():
    try:
        s, l1, r1, l2, r2 = map(int, input().split(' '))
        if l1 > r1 or l2 > r2:
            raise Exception
        return s, l1, r1, l2, r2
    except:
        print('Попробуйте снова')
        custom_input()


print('Введите 5 целых чисел')
s, l1, r1, l2, r2 = custom_input()

if l1 + l2 <= s <= r2 + r1:
    max_l = max(l1, l2)
    min_l = min(l1, l2)
    min_r = min(r1, r2)
    max_r = max(r1, r2)

    if min_l <= s - max_l <= max_r:
        print(max_l, s - max_l)
    else:
        print(min_r, min_r + s)
else:
    print('-1')
