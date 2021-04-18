import copy
from math import sqrt
from random import random
from typing import overload


def ВozoSort(a, b, c, flag: bool = True):
    temp = BozoSort([a, b, c], flag)
    return temp[0], temp[1], temp[2]


@overload
def BozoSort(lst: list, flag: bool = True) -> list:
    ...


@overload
def BozoSort(matrix, flag: bool = True) -> list:
    ...


def BozoSort(par, flag: bool = True):
    if isinstance(par[0], list):
        matrix = copy.deepcopy(par)
        temp = matrix[0]
        for i in range(1, len(matrix)):
            temp.extend(matrix[i])
        temp = BozoSort(temp, flag)

        matrix = [temp[i:i + len(matrix)] for i in range(0, len(temp), len(matrix))]

        return matrix
    else:
        lst = par
        length = len(lst)
        while not is_sorted(lst, flag):
            i1 = randomize(length)
            i2 = randomize(length)
            temp = lst[i1]
            lst[i1] = lst[i2]
            lst[i2] = temp
        return lst


def is_sorted(lst, flag: bool):
    if flag:
        for i in range(0, len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True
    else:
        for i in range(0, len(lst) - 1):
            if lst[i] < lst[i + 1]:
                return False
        return True


def randomize(length):
    return int(random() * length)


def custom_input():
    try:
        a = int(input())
        if not 4 <= a <= 100:
            raise Exception
        if not sqrt(a) ** 2 == a:
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
print(BozoSort(arr))
print(BozoSort(arr, flag=False))

m = [arr[i:i + int(sqrt(n))] for i in range(0, n, int(sqrt(n)))]
print(BozoSort(m))
print(BozoSort(m, flag=False))

print(ВozoSort(arr[0], arr[1], arr[2]))
print(ВozoSort(arr[0], arr[1], arr[2], flag=False))
