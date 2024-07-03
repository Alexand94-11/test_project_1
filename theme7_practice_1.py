class Product:
    # Опишите инициализатор класса и метод get_info()
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_info(self):
        return f'{self.name} (в наличии: {self.amount})'


class Kettlebell(Product):
    # Опишите инициализитор класса и метод get_weight()
    def __init__(self, name, amount, weight):
        super().__init__(name, amount)
        self.weight = weight

    def get_weight(self):
        return self.get_info() + f'. Вес: {self.weight} кг'


class Clothing(Product):
    # Опишите инициализатор класса и метод get_size()
    def __init__(self, name, amount, size):
        super().__init__(name, amount)
        self.size = size

    def get_size(self):
        return self.get_info() + f'. Размер: {self.size}'


# Для проверки вашего кода создадим пару объектов
# и вызовем их методы:
small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())
