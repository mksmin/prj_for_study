class Shape:
    def get_area(self):
        print('Недостаточно данных')

    @property
    def area(self):
        return self.get_area()


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = self.validate_value(a)
        self.b = self.validate_value(b)

    @classmethod
    def validate_value(cls, value):
        if isinstance(value, (int, float)):
            return value
        raise TypeError(f'Value should be int or float, not {type(value)}')

    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


class Square(Rectangle):
    # def __init__(self, a):
    #     super().__init__(a, a) # Обращаемся к родительскому классу и его методу

    def __init__(self, a):
        self._a = self.validate_value(a)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = self.validate_value(value)

    # def get_area(self):
    #     return self.a * self.a
    @property
    def b(self):
        return self.a

    @b.setter
    def b(self, value):
        self.a = self.validate_value(value)


print(Shape)
print(Shape.mro())

print(Rectangle)
print(Rectangle.mro())

print(Square)
print(Square.mro())

rectangle = Rectangle(4, 5)
print(rectangle)
print(rectangle.get_area())
rectangle.a = 6
print(rectangle)
print(rectangle.get_area())

sq1 = Square(5)
print(sq1)
print(sq1.get_area())

sq1.a = 6
print(sq1)
print(sq1.get_area())

sq1.b = 7
print(sq1)
print(sq1.get_area())

sq1.b = 2
print(sq1)
sq1.a = 'abs'
print(sq1)
