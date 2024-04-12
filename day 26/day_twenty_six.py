cant = int(input())
t = []
for i in range(cant):
    n = int(input())
    if n == 1:
        t.append('Not prime')
    else:
        if n % 2 == 0 and n > 2:
            t.append('Not prime')
        else:
            for _ in range(3, int(n ** 0.5 + 1), 2):
                if n % _ == 0:
                    t.append('Not prime')
                    break
            else:
                t.append('Prime')


for i in range(cant):
    print(t[i])
