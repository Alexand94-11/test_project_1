def fibonacci(n):
    # Допишите функцию.
    for number in range(n):
        if number == 0:
            yield number
            element_first = number
        elif number == 1:
            yield number
            element_second = number
        else:
            yield element_first + element_second
            delta = element_second
            element_second = element_first + element_second
            element_first = delta


sequence = fibonacci(10)
for number in sequence:
    print(number)
