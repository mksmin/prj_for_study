"""
This is doc for this module
"""

some_object = object()
print(some_object)

long_string = """
hello world!
"""


def my_func(a, b):
    """
    This is myfunc docstring
    >>> my_func(1, 2)
    This func swaps a and b
    """
    return b, a


def hello():
    """
    This is hello doc
    """


# help(my_func)

print(hello.__doc__)


class User:
    """
    """

user1 = User()
print(User)
print(user1)
print(type(user1))
print(User.mro())

user1.name = 'John'
print("name:", user1.name)
print("user1 dict", user1.__dict__)

