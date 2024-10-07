from pydantic import BaseModel, ValidationError
from datetime import datetime


class Point(BaseModel):
    x: int
    y: int


class User(BaseModel):
    id: int
    age: int = None
    name: str = 'John Doe'
    signup_dt: datetime = None
    friends_ids: list[int] = []
    active: bool = True
    points: list[Point] = []

    def add_friend(self, friend_id: int) -> None:
        self.friends_ids.append(friend_id)


def demo_user():
    user = User(
        id=1,
        age=23,
        name='User demo',
        signup_dt=1728307969
    )
    print(repr(user))
    john = User(
        id=2,
        age=22,
        friends_ids=[1, 3, '4', b'5'],
        points=[Point(x=1, y=2)],
        signup_dt='2022-11-15T22:30:42'
    )
    print(repr(john))
    user.add_friend(100)
    print(repr(user))
    print(repr(john))

    try:
        User(friends_ids=[5, "abc", 3],
             signup_dt='today',
             points=[(1, 2)])
    except ValidationError as e:
        print(e.json())

    user_data = {
        "id": 1,
        "age": 23,
        "name": "Sam",
        "points": [{"x": 1, "y": 2}],
        "active": False,
    }
    sam = User(**user_data)
    print(repr(sam))


def demo_point():
    p = Point(x=1, y=2)
    print(p)

    p1 = Point(x='1', y='2')
    print(p1)


def main():
    demo_point()
    demo_user()
    print(datetime.now().timestamp())


if __name__ == '__main__':
    main()
