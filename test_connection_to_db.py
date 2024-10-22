from functools import wraps
from typing import Optional


def connection(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        print('Подключение к БД')
        session = 'Привет'
        return function(session, *args, **kwargs)

    return wrapped


class User:
    name: str

    def create(self, session):
        print(session + ', ', self.name)

    def delete(self, session):
        print(session + ', ', self.name + '! Ты удален')


def create_user(session, object_: User, *args, **kwargs):
    object_.create(session)


def delete_user(session, object_: User, *args, **kwargs):
    object_.delete(session)


@connection
def main_connector(session,
                   object_: Optional[User], is_create, is_delete):
    if is_create:
        create_user(session, object_=object_)
    if is_delete:
        delete_user(session, object_=object_)


def main():
    user1 = User()
    user1.name = 'Max'
    user2 = User()
    user2.name = 'Dima'
    user3 = User()
    user3.name = 'Anna'

    main_connector(object_=user1, is_create=True, is_delete=True)
    main_connector(object_=user2, is_create=False, is_delete=True)
    main_connector(object_=user3, is_create=True, is_delete=False)


if __name__ == '__main__':
    main()