"""
Сокрытие имени
"""

class User:
    def __init__(self, name):
        self.name = name
        self._password = None


u = User('John')
print(u.name, u._password)
u._password = 'spam and eggs'
print(u.name, u._password)


class User:
    def __init__(self, name):
        self.name = name
        self.__password = "Abc"

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        print('set password', value)
        self.__password = hash(value)


class Manager(User):
    pass

u = User('John')
# print(u.name, u.__password)
print(u.name, u.password)
print(u.name)
print(u.__dict__)
print(u._User__password)

u.__password = 'secret'
print(u.name, u.password)
print(u.__dict__)
print(u.name, u.__password)

u.password = "supersectey"
print(u.name, u.password)
print(u.__dict__)
print()
print()


m1 = Manager('Admin')
print(m1.name, m1.password)
print(m1.__dict__)
m1.password = "adminpass"
print(m1.password, m1.name)
print(m1.__dict__)
print(m1.password)