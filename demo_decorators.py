from typing import Callable, Any, Optional
from functools import wraps

CallbackType = Callable[..., Any]


# декоратор как класс с методами
class Decorator:
    def __init__(self, *, name: Optional[str] = None):
        self.message = Event(router=self)


class Event:
    def __init__(self, router: Decorator):
        self.router: Decorator = router

    def __call__(
            self,
            *args_method,
            **kwargs_method
    ):
        all_agruments_method = list(args_method) + list(kwargs_method.keys())
        print(f'{all_agruments_method = }')

        def connection(callback: CallbackType):
            @wraps(callback)
            def wrapper(*args, **kwargs):
                all_agruments_func = list(args) + list(kwargs)
                print(f'{all_agruments_func = }')

                result = callback(*args, **kwargs)
                print(f'wrapper end')

                return result

            return wrapper

        return connection


router = Decorator()


@router.message('foo bar', maxs='cool')
def test_func(*args, a=1):
    print('func wrapped')
    print(f'a is {a = }')


test_func(1, 2, 3, a=5)


# декоратор с аргументами:
def my_dec(*arg):
    def inner_decorator(f):
        def wrapped(*args, **kwargs):
            print('до функции')
            print(f'аргументы: {arg}')
            response = f(*args, **kwargs)
            print('после функции')
            return response

        return wrapped

    return inner_decorator


@my_dec('foo', 'bar')
def my_func(a, b):
    print('внутри функции')
    print(f'Аргументы функции: {a = }, {b = }')
    return a + b


res = my_func(2, 3)
print(f'{res = }')
