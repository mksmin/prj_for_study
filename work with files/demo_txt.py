FILE_PATH = 'file.txt'


def main():
    # f = open(FILE_PATH, 'w')
    # f.write('Hello\n')
    # f.close()

    with open(FILE_PATH, 'w') as f:
        f.write('Hello World\n')

    with open(FILE_PATH, 'r') as f:
        print(f.readlines())
        print(f.read())
        print(f.readline())

    with open(FILE_PATH, 'a') as f:
        f.write('Hello again\n')
        f.writelines(['cats\n', 'dogs\n'])

    with open(FILE_PATH, 'r') as f:
        for line in f:
            print(line, end='')
    print()



if __name__ == '__main__':
    main()