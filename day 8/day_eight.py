def backwards(n_: int, arr_: list) -> str:
    s = ''
    for i in range(n_):
        n_ -= 1
        s += f'{arr_[n_]} '

    return s


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(backwards(n, arr))
