def multiples(n_: int) -> str:
    multi = ''
    for i in range(10):
        multi += f'{n_} x {i + 1} = {n_ * (i + 1)}\n'
    return multi


if __name__ == '__main__':
    n = int(input().strip())
    print(multiples(n))