from typing import Optional


class User:
    def __init__(
            self,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            username: Optional[str] = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # Опишите метод класса with_name.
    @classmethod
    def with_name(
        cls,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None
    ):
        return User(first_name, last_name)

    # Опишите метод класса with_username.
    @classmethod
    def with_username(cls, username):
        try:
            if User.is_username_allowed(username):
                return User(None, None, username)
            else:
                raise ValueError
        except ValueError:
            print('Некорректное имя пользователя')

    # Опишите статический метод класса is_username_allowed.
    @staticmethod
    def is_username_allowed(username: str):
        without_up = str.lower(username)
        if without_up.find('admin') != 0:
            return True
        else:
            return False

    # Опишите метод-свойство full_name.
    @property
    def full_name(self):
        if self.first_name is not None:
            return self.first_name + ' ' + self.last_name
        elif self.username is not None:
            return '@' + self.username


stas = User.with_name('Стас', 'Басов')
print(stas.full_name)

# Попробуем создать пользователя с "запрещённым" именем.
ne_stas = User.with_username('admin_nestas_anonymous')

not_admin = User.with_username('not_admin')
print(not_admin.full_name)

ne_stas_2 = User.with_username('admin')
