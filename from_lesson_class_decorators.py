class Robot:
    # Состояние батареи базовой станции:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    # Декорируем и изменяем метод update_base_battery_status(),
    # чтобы менять значение атрибута не в объекте, а в классе:
    @classmethod
    def update_base_battery_status(cls, new_status):  # Указываем аргумент cls.
        """Обновляет состояние батареи базовой станции."""
        # Присваиваем новое значение атрибуту класса.
        cls.base_battery_status = new_status

    def report(self):
        """Печатает в консоли состояние батареи базовой станции."""
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )

    @staticmethod
    def predict_battery_lifetime(current_capacity, charge_cycles):
        """
        Прогнозирует срок службы аккумулятора
        на основе текущей ёмкости и количества циклов зарядки.
        """
        # Пусть максимальная ёмкость нового аккумулятора будет равна 5000 мАч
        max_capacity = 5000
        return (current_capacity / max_capacity) * (1000 - charge_cycles)

    # Для определения метода как свойства применяют декоратор @property
    @property
    def identifier(self):
        """Вычисляет уникальный идентификатор робота на основе его имени."""
        # Преобразование имени в числовое представление:
        return sum(ord(char) for char in self.name)


# Создаём двух роботов:
robot1 = Robot('R2-D2')
print(robot1.identifier)
robot2 = Robot('C-3PO')
print(robot2.identifier)

# Печатаем состояние батареи:
robot1.report()
robot2.report()

# Обновляем статус батареи в классе: обращаемся не к объекту, а к классу.
Robot.update_base_battery_status(80)

# Снова печатаем состояние батареи:
robot1.report()
robot2.report()

# Вызов статического метода через имя класса:
battery_lifetime = Robot.predict_battery_lifetime(4000, 100)
print(
    'Прогноз срока службы аккумулятора: '
    f'осталось {battery_lifetime:.0f} циклов зарядки.'
)

# Статический метод доступен и в объекте:
r2d2_battery_lifetime = robot1.predict_battery_lifetime(3500, 150)
print(
    'Прогноз срока службы аккумулятора: '
    f'осталось {r2d2_battery_lifetime:.0f} циклов зарядки.'
)
