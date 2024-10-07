from collections import namedtuple

# class User:
#     def __init__(self, user_id, age):
#         self.user_id = user_id

Point = namedtuple('Point', ['x', 'y'])

Useridandage = namedtuple('User', 'user_id, age')
User = namedtuple('User', 'user_id, age, email, username, full_name')

print(User)


def demo_point():
    p = Point(2, y=3)
    print(p)


def demo_user():
    u = User(
        user_id=123,
        age=20,
        username='John',
        email='john@example.com',
        full_name='john smith'
    )
    print(u)
    print(u.age)
    print(u.user_id)
    print(u[0], u[1])

    user_id, age, *_ = u
    print(user_id, age)
    print(_)


def demo_user_and_point():
    p = Point(x=40, y=50)
    u = Useridandage(user_id=40, age=50)
    print('p == u:', p == u)


def main():
    demo_user()
    demo_point()
    demo_user_and_point()


if __name__ == '__main__':
    main()
