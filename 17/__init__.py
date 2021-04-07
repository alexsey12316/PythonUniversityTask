def custom_input():
    try:
        print('\nВведите число')
        a = int(input())
        if not -36 <= a <= 36:
            raise Exception
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


n = custom_input()
history = [0] * 37
queue = []
reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
red_count = 0
black_count = 0
while n > 0:
    history[n] += 1
    m = max(history)
    if m > 0:
        for i in range(0, 37):
            if history[i] == m:
                print(i, end=' ')
    print('')
    queue.append(n)
    if len(queue) > 12:
        queue.pop(0)
    for i in range(0, 37):
        if not queue.__contains__(i):
            print(i, end=' ')
    if reds.__contains__(n):
        red_count += 1
    elif n != 0:
        black_count += 1
    print(' ')
    print( red_count, ' ', black_count)
    n = custom_input()
