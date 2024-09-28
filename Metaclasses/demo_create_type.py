@classmethod
def echo_name(cls):
    print(cls.__name__)


def echo_foobar(self):
    print('foobar value:', self.foobar)


Foo = type('Foo', (), {"foobar": "spam and eggs",
                       "echo_name_1": echo_name,
                       "echo_foobar": echo_foobar})

print(Foo)
print(Foo.mro())
print(type(Foo))


foo = Foo()
print(foo)
Foo.echo_name_1()
foo.echo_foobar()

print(foo.__dict__)
print(dir(Foo))
print(Foo.foobar)