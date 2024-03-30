import os


def factorial(n_: int) -> int:
    if n_ <= 1:
        return 1
    else:
        return n_ * factorial(n_ - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
