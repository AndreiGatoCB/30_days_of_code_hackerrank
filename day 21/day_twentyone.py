#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    b = int()

    while a != sorted(a):
        for i in range(len(a) - 1):
            while a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                b += 1
    print(f'Array is sorted in {b} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}')
    # Write your code here
