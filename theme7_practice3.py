class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10

    def get_price(self, source_price):
        final_price = source_price * (100 - self.__discount) / 100
        return round(final_price, 2)
    # Реализуйте методы get_price() и set_discount().

    def set_discount(self, new_discount):
        if new_discount < 80:
            self.__discount = new_discount
        else:
            self.__discount = 80


customer = Customer("Иван Иванович")
customer.get_price(100)
customer.set_discount(20)
customer.get_price(100)
