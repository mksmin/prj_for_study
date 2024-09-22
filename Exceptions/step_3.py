class MyException(Exception):
    pass


print(MyException, MyException.mro())

err = MyException('some error text')
print('Hello')
print("exc", err, repr(err))

# raise err
raise MyException

print('never')