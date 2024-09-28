class Foo:
    """
    My Foo class
    """

    foobar = "spam and eggs"

    def echo_name(self):
        print(self.__class__.__name__)

    @classmethod
    def echo_foo(cls):
        print(cls.__name__)


print(Foo)
print(Foo.mro())
foo = Foo()
print(foo)
foo.echo_name()
foo.echo_foo()
print("type foo:", type(foo))
print("type Foo:", type(Foo))
print("type of type:", type(type))


