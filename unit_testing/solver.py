

class Solver:
    EXC_TEXT_INVALID_TYPE = "can't multiply sequence by non-int of type 'str'"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        result = self.a + self.b
        print(f'result: {result}')
        return self.a + self.b

    def mul(self):
        if not (
            isinstance(self.a, (int, float))
            and isinstance(self.b, (int, float))
        ):
            raise TypeError(self.EXC_TEXT_INVALID_TYPE)
        return self.a * self.b
