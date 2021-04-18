def custom_input():
    try:
        a = int(input())
        if not 1 <= a <= 100000:
            raise Exception
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


n = custom_input()


def list_input():
    try:
        a = [eval(i) for i in input().split(' ')]
        if not len(a) == n:
            raise Exception
        return a
    except:
        print('Попробуйте снова')
        return list_input()


arr = list_input()

result = []

for i in arr:
    result.append(i)
    result.sort(reverse=True)
    if len(result) == 6:
        result.pop(0)
    print(result)
