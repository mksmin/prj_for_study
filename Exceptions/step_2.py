def div_safe(a, b):
    print('entering div a, b', [a, b])
    try:  # попробуй выполнить
        c = a / b
    except ZeroDivisionError:  # если ошибка деления на ноль, то сделай
        print('Please dont divide by zero')
        return None
    except TypeError as e:  # если ошибка типа, то сделай
        print('oops. Type Error', e)
    else:  # если ошибок не возникло, тогда сделай
        print('successfully divided')
        return c
    finally:  # независимо от того, что произойдет сделай: (даже есть return)
        print('finally for', [a, b])

    print('leaving func for', [a, b])


print(div_safe(3, 4))
print()
print(div_safe(10, 2))
print()
print(div_safe(10, 0))
print()
print(div_safe(10, '2'))
