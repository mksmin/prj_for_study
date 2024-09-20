class User:
    def __init__(self):
        self.name = None
        self.age = None


user1 = User()
print(user1.__dict__)
print(user1.name)
user1.name = "John"
print(user1.name)