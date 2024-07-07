# Импортируйте необходимые модули.
from datetime import datetime
# Укажите два параметра функции:

DATE_FORMAT = '%d.%m.%Y'


def validate_record(name, birth_date):
    # Напишите код, верните булево значение.
    try:
        datetime.strptime(birth_date, DATE_FORMAT)
        return True
    except ValueError:
        print('Некорректный формат даты в записи: ' + name + ', ' + birth_date)
        return False


# Укажите параметры функции:
def process_people(data):
    # Объявите счётчики.
    good_count = 0
    bad_count = 0
    for employee in data:
        name, birth_date = employee
        if validate_record(name, birth_date):
            good_count += 1
        else:
            bad_count += 1
    result = {
        'good': good_count,
        'bad': bad_count
    }
    print('Корректных записей:', result['good'])
    print('Некорректных записей:', result['bad'])
    return result
    # в каждой паре значений из списка data
    # проверьте корректность формата даты рождения
    # и в зависимости от результата проверки увеличьте один из счётчиков.


data = [
    ('Иван Иванов', '10.01.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]
statistics = process_people(data)
# Выведите на экран информацию о корректных и некорректных записях
# в таком формате:
# Корректных записей: <число>
# Некорректных записей: <число>
