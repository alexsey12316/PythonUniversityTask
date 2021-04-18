def custom_input():
    try:
        a = int(input())
        if not 1 <= a <= 10 ** 9:
            raise Exception
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


def print_factorization(n: int) -> None:
    dic = {}
    i = 2
    while i <= n:
        if (n / i).is_integer():
            if not dic.__contains__(i):
                dic[i] = 0
            dic[i] += 1
            n = n / i
        else:
            i += 1
    output = ''
    for k in dic:
        output += f'{k}{f"^{dic[k]}*" if dic[k] > 1 else "*"}'
    print(output[:-1])


print_factorization(custom_input())
