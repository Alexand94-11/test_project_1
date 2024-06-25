from math import sqrt
from typing import Optional


def add_numbers(first: int, second: int) -> int:
    return first + second


def calculate_square_root(number: float) -> float:
    return round(sqrt(number), 2)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return None
    else:
        result = calculate_square_root(your_number)
        return ('Мы вычислили квадратный корень из введённого вами числа.'
                f' Это будет: {result}')


number_1 = 10
number_2 = 5
print('Сумма чисел: ', add_numbers(number_1, number_2))
print(calc(25.5))
