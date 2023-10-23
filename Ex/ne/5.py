#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findLargestSquareSize' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY samples as parameter.
#
def make_flag(length, samples):
    flag = [[-1 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        temp = -1
        for j in range(length - 1, -1, -1):
            if samples[i][j] == 1:
                if temp == -1:
                    temp = j
                flag[i][j] = temp
            else:
                temp = -1
    return flag


def check(space, x, y, length, flag):
    for i in range(x, x + length):
        if flag[i][y] - y + 1 < length:
            return False
    return True


def findLargestSquareSize(samples):
    length = len(samples)
    flag = make_flag(length, samples)

    for k in range(length, 0, -1):
        for i in range(length - (k - 1)):
            for j in range(length - (k - 1)):
                if check(samples, i, j, k, flag):
                    return k
    return 0


if __name__ == '__main__':
    samples_rows = int(input().strip())
    samples_columns = int(input().strip())

    samples = []
    for _ in range(samples_rows):
        samples.append(list(map(int, input().rstrip().split())))

    result = findLargestSquareSize(samples)

    print(result)
