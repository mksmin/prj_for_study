import os

BASE_DIR = os.path.dirname(__file__)
IS_WINDOWS = "nt" in os.name

def demo_paths():
    print(__file__)
    print(BASE_DIR)
    print("is windows?", IS_WINDOWS)
    print("os path sep:", os.path.sep)

    print()

    folder_name = 'pictures'
    file_name = 'cat.jpg'
    print(''.join(('foo', 'bar')))
    print(os.path.join(BASE_DIR, folder_name, file_name))


def demo_cwd():
    cwd = os.getcwd()
    print(f'{cwd = }')


def demo_list_dir():
    print(os.listdir('..'))
    print(os.listdir('../app'))

    filename = '../work with files/file.txt'
    if os.path.isfile(filename):
        os.unlink(filename)

    with open(filename, 'w') as f:
        f.write('hello \n')

    with open(filename) as f:
        print(f.readlines())
        print('HUY')

def main():
    print("Hello World")


if __name__ == "__main__":
    main()
    demo_paths()
    demo_cwd()
    demo_list_dir()

print("__name__", __name__)