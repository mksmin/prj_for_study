from functools import reduce, lru_cache, partial
import operator


def mul(a, b):
    print(f'{a = }, {b = }, a * b = {a * b}')
    return a * b


def demo_reduce():
    print(sum(range(5)))
    result = reduce(lambda a, b: a + b, range(5))
    print(result)

    result = reduce(mul, [2,4,5,9,15])
    print(result)

    result = reduce(operator.mul, [2, 4, 5, 9, 15])
    print(result)

    line = reduce(operator.concat, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    print(line)


def demo_reduce_pro():
    # print(min(1, 2))
    # print(max(1, 2))

    numbers = (2, 3, 4, 0, 7, 5)

    print(reduce(min, numbers))
    print(reduce(max, numbers))

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def demo_fib():
    print([fib(i) for i in range(15)])
    print(list(map(fib, range(10))))


def demo_partial():
    mul_2 = partial(mul, 2)
    print(mul_2(3))

    mul_on_3 = partial(mul, b=3)
    print(mul_on_3(4))

    print(pow(3, 2))

    square = partial(pow, exp=2)
    print(square(3))

def main():
    # demo_reduce()
    # demo_fib()
    # demo_partial()
    demo_reduce_pro()


if __name__ == '__main__':
    main()