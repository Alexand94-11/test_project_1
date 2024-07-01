# Родительский класс.
class Phone:

    # Атрибут базового класса.
    line_type = 'проводной'

    # Инициализатор базового класса.
    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value
        # Вот он - защищённый атрибут. Значением будет
        # ID ячейки памяти аргумента dial_type_value.
        self._serial_number = id(dial_type_value)

    # Метод базового класса.
    def ring(self):
        print('Дзззззыыыыыыыынь!')

    # Ещё один метод базового класса.
    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


'''
# Пример создания пустого дочернего класса, унаследованного от класса Phone.
class MobilePhone(Phone):
    pass
# ______________________________________________________
# Использование метода родительского класса:
mobile_phone = MobilePhone('сенсорный')
mobile_phone.ring()
# Выведется:
# Дзззззыыыыыыыынь!
'''
# Переопределение атрибута(line_type) и метода(ring()) родительского класса,
# добавление нового атрибута класса(battery_type),
# нового атрибута экземпляра класса(network.type)
# с использованием функции super() и нового метода(start_game())


class MobilePhone(Phone):
    # Переопределить значение атрибута line_type класса Phone.
    line_type = 'беспроводной'
    # Никаких сюрпризов - обычная переменная,
    # в которой хранится нужное значение.
    battery_type = 'Li-ion'

    # Инициализатор класса MobilePhone с новым параметром - network_type.
    # Пример использования родительского инициализатора
    def __init__(self, dial_type_value, network_type):
        # Новый атрибут объекта, который сделан приватным(можно обратиться
        # только внутри класса):
        self.__network_type = network_type
        # Вызов родительского инициализатора.
        super().__init__(dial_type_value)

    # Переопределить метод ring() класса Phone.
    def ring(self):
        print('Дзынь-дзынь!')

    # Новый метод.
    def start_game(self):
        print('Игра запущена!')

    # Здесь переопределён метод __str__ .
    def __str__(self):
        return f'У мобильного телефона {self.dial_type} тип набора номера'

    # Это публичный метод, в котором используется защищённый атрибут.
    # Метод определён в классе-наследнике, защищённые атрибуты можно
    # использовать напрямую в базовом классе и его наследниках.
    def get_info(self):
        print(f'Серийный №: {self._serial_number}, '
              # Из метода класса можно обратиться к приватному атрибуту.
              f'тип сети: {self.__network_type}')


# Экземпляры родительского класса Phone:
rotary_phone = Phone(dial_type_value='дисковый')
# Альтернативный вариант объявления экземпляра класса:
# rotary_phone = Phone('дисковый')
keypad_phone = Phone(dial_type_value='кнопочный')
# Экземпляр дочернего класса MobilePhone:
mobile_phone = MobilePhone('сенсорный', 'LTE')

# Распечатать значение атрибута line_type для объекта класса Phone.
print(rotary_phone.line_type)
# Вызвать метод ring() для объекта класса Phone.
rotary_phone.ring()

# Распечатать значение атрибута line_type для объекта класса MobilePhone.
print(mobile_phone.line_type)
# Вызвать метод ring() для объекта класса MobilePhone.
mobile_phone.ring()

# Вывод:
# проводной
# Дзззззыыыыыыыынь!
# беспроводной
# Дзынь-дзынь!

# Проверка работы переопределенного метода __str__:
print(mobile_phone)

# Обращение к защищенному атрибуту:
# Обращение через метод.
mobile_phone.get_info()
# Обращение напрямую.
print('Серийный номер телефона(объекта) keypad_phone:',
      keypad_phone._serial_number)
print('Серийный номер телефона(объекта) mobile_phone:',
      mobile_phone._serial_number)

# Вызов метода, в котором используется приватный атрибут:
mobile_phone.get_info()
# А вот вывести приватный атрибут на печать не получится - возникнет ошибка
# print(mobile_phone.__network_type)
# Чтобы обойти это ограничение, можно обратиться к приватному атрибуту
# по схеме: _ИмяКласса__ИмяАтрибута(считается плохой практикой):
# print('Обращение к приватному атрибуту через измененное имя:')
# print(mobile_phone._MobilePhone__network_type)
print('*********************************************************')
