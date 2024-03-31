if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    marr = []
    sum_arr = int()
    for _ in range(4):
        for j in range(4):
            hour_glass = []
            for i in range(3):
                hour_glass.append(arr[i][j])
                hour_glass.append(arr[i][j + 1])
                hour_glass.append(arr[i][j + 2])
            sum_arr = sum(hour_glass) - hour_glass[3] - hour_glass[5]
            marr.append(sum_arr)
        arr.remove(arr[0])
    print(max(marr))
