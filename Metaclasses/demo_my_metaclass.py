class MyMetaclass(type):
    def __new__(cls, name, bases, dct, *arts, **kwargs):
        print("new class", name)
        print("bases", bases)
        print("dct", dct)

        print("dct before:", dct)


        for key in dct.keys():
            # if key.startswith('__') and not key.endswith('__'):
            if key.startswith('_') and not key.endswith('__'):
                value = dct.pop(key)
                # dct[key[2:].upper()] = value
                dct[key.upper()] = value


        print("dct:", dct)
        dct["SPAM_AND_EGGS"] = "foobar"
        new_class = super().__new__(cls, name, bases, dct, *arts, **kwargs)
        return new_class


# Foo = MyMetaclass('Foo', (), {})
Foo = MyMetaclass('Foo', (), {"spam": "eggs"})
print(Foo)
print(Foo.mro())
print(MyMetaclass.mro(Foo))
print(type(Foo))
print(dir(Foo))
print(Foo.spam)

print("Foo.Spam_and_eggs", Foo.SPAM_AND_EGGS)

class Foo(object, metaclass=MyMetaclass):
    def __new__(cls, *args, **kwargs):
        print("new class", cls)

    def __init__(self, *args, **kwargs):
        self.__super_secret_value = 'fizzbuzz'

    # __super_secret_value = 'fizzbuzz'
    _another_super_secret_value = 'fizzbuzz'


print(Foo)
print(type(Foo))



print(dir(Foo))

print("Foo.Spam_and_eggs", Foo.SPAM_AND_EGGS)
print(Foo._ANOTHER_SUPER_SECRET_VALUE)
