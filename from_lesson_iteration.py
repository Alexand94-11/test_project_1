'''
# Генератор:
def short_sequence():
    num = 1
    while num < 5:
        yield num
        num += 1

for step in short_sequence():
    print(step)

# Так описывается список через list comprehension.
simple_list = [digit for digit in range(2)]

print(type(simple_list))
a = iter(simple_list)
print(a.__next__())
print(a.__next__())

# Выведется:
# <class 'list'>
# 0
# 1

# А так описывается генераторное выражение.
simple_generator = (digit for digit in range(2))

print(type(simple_generator))
print(simple_generator.__next__())
print(simple_generator.__next__())

# Выведется:
# <class 'generator'>
# 0
# 1
'''
# Задание:
# Создайте генераторное выражение, которое из списка чисел numbers
# возводит в квадрат те, что делятся на 3.
# Затем распечатайте сумму квадратов.

# Список для тестирования.
numbers = [1, 3, 4, 6, 9, 11]

'''
# Решение без генераторного выражения:
def generator_list(digits):
    for digit in digits:
        if digit % 3 == 0:
            yield digit**2
# Распечатайте сумму квадратов.
print(sum(generator_list(numbers)))
'''

# Решение с генераторным выражением:
generator_list = (digit**2 for digit in numbers if digit % 3 == 0)

# Распечатайте сумму квадратов.
print(sum(generator_list))
