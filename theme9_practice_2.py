# Напишите декоратор obfuscator
def obfuscator(func):
    def wrapper():
        result = func()
        name_list = list(result['name'])
        for letter in range(1, len(result['name']) - 1):
            name_list[letter] = '*'
        result['name'] = str.join('', name_list)
        password_list = list(result['password'])
        for letter in range(len(result['password'])):
            password_list[letter] = '*'
        result['password'] = str.join('', password_list)
        return result
    return wrapper


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())
