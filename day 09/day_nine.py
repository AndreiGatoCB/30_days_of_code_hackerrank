phone_book = {}
n = int(input())

input_lines = [input().split() for _ in range(n)]
phone_book.update({name: number for name, number in input_lines})

while True:
    try:
        name = input().strip()
        if name in phone_book.keys():
            print(f'{name}={phone_book[name]}')
        else:
            print('Not found')
    except EOFError:
        break

