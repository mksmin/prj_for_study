from dataclasses import dataclass


@dataclass(frozen=False)
class Point:
    x: int
    y: int

    def incr_both(self):
        self.x += 1
        self.y += 1

    def __add__(self, other: 'Point') -> 'Point':
        if isinstance(other, Point):
            return Point(x=self.x + other.x, y=self.y + other.y)
        raise TypeError(f'Other should be Point, not {type(other)}')

def demo_point():
    p1 = Point(1, 2)
    p2 = Point(3, y=4)
    print(p1, p2)

    p1.y = 5
    p1.x = 7
    print(p1)

    print(p2)
    p2.incr_both()
    print(p2)

    p3 = p1 + p2
    print(p3)


def main():
    demo_point()


if __name__ == '__main__':
    main()
