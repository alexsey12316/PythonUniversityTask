def custom_input():
    try:
        a = [int(i) for i in input().split(' ')]
        return a[0], a[1]
    except:
        print('Попробуйте снова')
        return custom_input()


def bmi(weight: float, height: float) -> float:
    return weight / height ** 2


def print_bmi(bmi: float):
    if bmi < 18.5:
        print('Underweight')
    elif bmi < 25:
        print('Normal')
    elif bmi < 30:
        print('Overweight')
    else:
        print('Obesity')


a, b = custom_input()
print_bmi(bmi(a, b / 100))
