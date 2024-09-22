class InvalidOperandError(ValueError):
    pass


print(InvalidOperandError, InvalidOperandError.mro())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str([self.x, self.y])

    def __repr__(self):
        return f"{self.__class__.__name__}(x = {self.x}, y = {self.y})"

    def add(self, p):
        if not isinstance(p, self.__class__):
            raise InvalidOperandError(f'Should be point, not be {type(p)}')
        return self.__class__(x=self.x + p.x, y=self.y + p.y)

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        if not isinstance(other, self.__class__):
            raise InvalidOperandError(f'Should be point, not be {type(other)}')

        self.x += other.x
        self.y += other.y
        return self


p1 = Point(2, 3)
p2 = Point(5, 6)

print(p1)
print(p2)
print([p1, p2])

p3 = p1.add(p2)
print(p3)

# p3 = p1.add([1, 2])
# print(p3)

p3 = p1 + p2
print(p3)
print(id(p3))
p3 += p1
print(p3)
print(id(p3))
