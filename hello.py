import sys

print('hello, steven')


def say_it():
    print('hello, steven')


if __name__ == '__main__':
    print(sys.argv[0])
    if len(sys.argv) >= 2:
        globals()[sys.argv[1]]()
