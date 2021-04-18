import re


class Drink:
    def __init__(self, name, price, volume):
        self.name = name
        self.price = price
        self.volume = volume

    def __gt__(self, other):
        return self.price / self.volume > other.price / other.volume

    def __ge__(self, other):
        return self.price / self.volume >= other.price / other.volume

    def __lt__(self, other):
        return self.price / self.volume < other.price / other.volume

    def __le__(self, other):
        return self.price / self.volume <= other.price / other.volume


def custom_input():
    try:
        a = int(input())
        return a
    except:
        print('Попробуйте снова')
        return custom_input()


def custom_input2():
    try:
        data = input().split(' ')
        if not re.match('^[A-Za-z]+$', data[0]):
            raise Exception
        return data[0], int(data[1]), int(data[2])
    except:
        print('Попробуйте снова')
        return custom_input2()


print('Введите n')
n = custom_input()
print('Введите k')
k = custom_input()

list_of_drinks = []

print('Введите напитки')
for i in range(0, k):
    list_of_drinks.append(Drink(*custom_input2()))

# n = 110
# list_of_drinks = [Drink('vodka', 40, 1), Drink('beer', 30, 2), Drink('alcohol', 80, 1), Drink('баярышник', 20, 1)]

list_of_drinks.sort()

count = 0
for i in range(0, len(list_of_drinks)):
    while n >= list_of_drinks[i].price:
        count += 1
        n -= list_of_drinks[i].price

    if count > 0:
        print(f'{list_of_drinks[i].name} {count}')
        print(list_of_drinks[i].volume * count)
    count = 0

print(n)
