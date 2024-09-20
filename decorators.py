from functools import wraps, lru_cache
from timeit import default_timer


def number_power(number, power=2):
    return number ** power


d = number_power(3, 4)

numbers = (4, 5)
c = number_power(*numbers)
print(c)

params = {
    "power": 4,
    "number": 3,
}

c = number_power(**params)
print(c)


def power_numbers(*numbers, power=2):
    return [number ** power for number in numbers]


c = power_numbers(*range(5))
print(c)


def my_function():
    print('My function runs')


def my_decorator(func_to_decorate):
    print('A. My decorator: create a new func')

    def replacement_function():
        print('B. Running replacement function')
        func_to_decorate()
        print('C. Finished running replacement function')

    print('D. Created a replacement function')
    return replacement_function


my_function = my_decorator(my_function)
print()
my_function()
print()


@my_decorator
def small_func():
    print('Small func')


def my_dec(func):
    @wraps(func)
    def wrapper():
        print('call func', func)
        func()
        print('finished wrapper')

    return wrapper


@my_dec
def some_func():
    print('Some func called')


print(some_func)
some_func()

print()
print()


def dec_with_one_arg(func):
    @wraps(func)
    def wrapper(arg):
        print('Call func', func, 'with arg', arg)
        result = func(arg)
        print('-- result:', result)
        return result

    return wrapper


@dec_with_one_arg
def cube(num):
    return num ** 3


def show_timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        result = func(*args, **kwargs)
        end_time = default_timer()
        total_time = end_time - start_time
        print('Executed func',
              func,
              'in {:.10f} sec.'.format(total_time),
              'and got',
              result
              )
        return result

    return wrapper


@show_timing
def power_nums(*nums, power=2):
    return [n ** power for n in nums]


d = power_nums(9, 6, 3, power=4)

print()


@lru_cache
@show_timing
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def cache_one_arg(func):

    func._cache = {}

    @wraps(func)
    def wrapper(arg):
        if arg in func._cache:
            return func._cache[arg]

        result = func(arg)
        func._cache[arg] = result
        return result
    return wrapper


@cache_one_arg
@show_timing
def square(num):
    return num ** 2

print(square)

square(2)
square(3)
print(square(2))

print(square._cache)

