from pathlib import Path



def demo_cwd():
    cwd= Path.cwd()
    print(f'{cwd = }')

    print("Path.cwd()")

def main():
    demo_cwd()


if __name__ == '__main__':
    main()