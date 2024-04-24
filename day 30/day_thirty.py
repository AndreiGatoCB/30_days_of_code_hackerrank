import os

def bitwiseAnd(N, K):
    r = int()
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            result = i & j
            if result < K and result > r:
                r = result
                if r == K - 1:
                    return r
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
