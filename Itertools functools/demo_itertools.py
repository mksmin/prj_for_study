from itertools import (
    zip_longest,
    cycle,
    chain,
    count,
    combinations,
    combinations_with_replacement,
    permutations,
    repeat
)


names = ['Sam', "Nick", "John"]
names_female = ['Ann', 'Kate']
surnames = ['Smith', 'Black', 'White', 'Bond']
emails = ['a@b.com', 'name@example.com', 'surname@google.com']

all_names = names + names_female
names_male_and_female = [names, names_female]

def demo_zip():
    pairs = zip(names, surnames)
    print(list(pairs))

    names_pairs = [('Sam', 'Smith'), ('Nick', 'Black'), ('John', 'White')]
    result = list(zip(*names_pairs))
    print(result)

    result3 = zip(names, surnames, emails)
    print(list(result3))

    source = [('Sam', 'Smith', 'a@b.com'), ('Nick', 'Black', 'name@example.com'), ('John', 'White', 'surname@google.com')]
    result2 = list(zip(*source))
    print(result2)


def demo_zip_longest():
    collection = list(zip_longest(names, surnames, emails, fillvalue=""))
    print(collection)


def demo_cycle():
    emails_demo = ["a@b.com", "c@d.com"]
    c= cycle(emails_demo)
    pairs = zip(names, c)
    print(list(pairs))

    # pairs = zip(surnames, cycle(emails_demo))
    pairs = zip(surnames, c)
    print(list(pairs))


def demo_chain():
    print(names_male_and_female)
    print(list(chain(names_male_and_female)))
    print(list(chain.from_iterable(names_male_and_female)))
    print(list(chain(*names_male_and_female)))


def demo_count():
    # c = count()
    c = count(1, step = 2)
    # print(c)
    # print(next(c))
    # print(next(c))
    # print(c)
    result = zip(
        chain.from_iterable(names_male_and_female),
        c
    )
    print(list(result))


def demo_combinations():
    nums = list(range(3))
    print(nums)
    print(list(combinations(nums, 2)))

    print(f'{all_names = }')
    print(f'{names_male_and_female = }')

    print(list(combinations(names, 2)))
    print(list(combinations(all_names, 3)))


def demo_combinations_with_rp():
    print(list(combinations(range(3), 2)))
    print(list(combinations_with_replacement(range(3), 2)))
    print(list(combinations_with_replacement(range(3), 3)))
    print(list(combinations_with_replacement(names_female, 2)))


def demo_permutations():
    print(list(permutations(names, 2)))
    print(list(permutations(range(3), 2)))
    print(list(permutations(names, 3)))


def demo_repeat():
    c = cycle([3])
    print(list(map(pow, range(5), c)))
    print(c)

    r = repeat(3)
    print(list(map(pow, range(5), r)))
    print(r)


def main():
    # demo_zip()
    # demo_zip_longest()
    # demo_cycle()
    # demo_chain()
    # demo_count()
    # demo_combinations()
    # demo_combinations_with_rp()
    # demo_permutations()
    demo_repeat()


if __name__ == '__main__':
    main()