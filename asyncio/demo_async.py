import asyncio
import time


async def fun1(x):
    print(x ** 2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun2(x):
    print(x ** 0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    print(type(task1))
    print(task1.__class__.__bases__)

    await task1
    await task2


# print(time.strftime('%X'))
#
asyncio.run(main())
#
# print(time.strftime('%X'))


class Gen1:
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number == 20:
            raise StopIteration
        else:
            return self.number


def custom():
    number = 0
    while True:
        print(f'Сейчас отдаю: {number}')
        yield number
        number += 1
        print(f'number стал {number}')
        if number == 11:
            break
        else:
            print(f'-- все еще выполняется ')

    print(f'Совсем закончил')


b = Gen1()

# print(b)
# print(next(b))
# print(type(next(b)))
#
# print(b.custom())
# print(type(b.custom))
# print(type(b.custom()))

# for i in range(30):
#     try:
#         print(f'Начал {next(b)}')
#         print(f'{i + 1} вызов = {i + 1}')
#     except StopIteration:
#         print('буквы закончились')
#         print()
#         break

print('начинаю другой делать ежже ')

g = custom()
for i in range(20):

    ds = next(g)
    print(f'ds = {ds}')
    # except StopIteration:
    #     print()
    #     print('буквы закончились')
    #     break

    # print(f'Начал {ds}')
    # print(f'{i + 1} вызов = {i + 1}')
