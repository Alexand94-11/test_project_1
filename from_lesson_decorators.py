'''
def outer_function(func):
    # Вызываем функцию, полученную в аргументе func:
    result = func('Стас')
    print(result)


def say_hello(name):
    return f'Привет, {name}!'


# Передаём say_hello как объект - без скобок!
outer_function(say_hello)


# Пример использования декоратора джуна:
import time


# Функция time_of_function() примет на вход
# любую другую функцию и засечёт время её выполнения.
def time_of_function(func):
    start_time = time.time()
    # Вызываем функцию, полученную в аргументе:
    result = func()
    execution_time = round(time.time() - start_time, 3)
    print(f'Время выполнения: {execution_time} сек.')
    # Возвращаем результат выполнения функции, полученной в аргументе:
    return result


def sleep_one_sec():
    time.sleep(1)
    return 'Функция sleep_one_sec() завершила вычисления.'


# Вызываем функцию time_of_function(), передаём в аргументе
# объект функции sleep_one_sec (без скобок!):
decorator_result = time_of_function(sleep_one_sec)

# Печатаем результат, который вернула функция time_of_function().
# Но на самом-то деле time_of_function() вернула
# результат выполнения sleep_one_sec(), вызванной внутри декоратора:
print(decorator_result)
'''

import time


# Декоратор объявляется до декорируемой функции.
def time_of_function(func):
    # В декораторе есть вложенная функция.
    def wrapper():
        start_time = time.time()
        result = func()
        execution_time = round(time.time() - start_time, 3)
        print(f'Время выполнения: {execution_time} сек.')
        return result
    # Декоратор возвращает вызываемый объект (callable object),
    # в нашем случае - функцию.
    return wrapper


# Имя функции-декоратора (с символом @)
# ставится перед объявлением декорируемой функции.
@time_of_function
def sleep_one_sec():
    time.sleep(1)
    return 'Функция sleep_one_sec() завершила вычисления.'


# После декорирования любой вызов функции sleep_one_sec()
# будет автоматически сопровождаться измерением времени её выполнения.
sleep_one_sec()
