with open('final.txt', 'r') as f:
    name = f.read()


def hello(text):
    print(f'Привет, {text}')


if __name__ == '__main__':
    hello(name)
    