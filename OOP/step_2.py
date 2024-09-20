class User:
    name = None
    age = None

user1 = User()
print(f'{user1.name = }')
print(user1.__dict__)

user1.name = 'John'
print(f'{user1.name = }')
print(user1.__dict__)

user2 = User()
user2.name = 'Jack'
user2.age = 25
print(user2.__dict__)