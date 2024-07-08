'''
people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']


def say_to_all(func, sequence):
    for item in sequence:
        func(item)


# Этот вызов для каждого имени из списка должен напечатать
# строчку Привет, <имя>!
say_to_all(lambda name: print(f'Привет, {name}!'), people)
# Этот вызов для каждого имени из списка должен напечатать
# строчку До завтра, <имя>!
say_to_all(lambda name: print(f'До завтра, {name}!'), people)
'''
people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']


def say_to_all(func, sequence):
    for item in sequence:
        func(item)


say_to_all(lambda name: print(f'Здравствуй, {name}!')
           if name[0] == 'С' else print(f'Привет, {name}!'), people)
