#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


#
# Complete the 'reachTheEnd' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER maxTime
#

def reachTheEnd(grid, maxTime):
    q = deque()
    q.append([0, 0, 0])
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    while q:
        x, y, c = q.popleft()
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            if c <= maxTime:
                return "Yes"
            else:
                return "No"
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx > len(grid) - 1 or ny < 0 or ny > len(grid[0]) - 1 or grid[nx][ny] == '#':
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny, c + 1])
    return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_count = int(input().strip())

    grid = []

    for _ in range(grid_count):
        grid_item = input()
        grid.append(grid_item)

    maxTime = int(input().strip())

    result = reachTheEnd(grid, maxTime)

    fptr.write(result + '\n')

    fptr.close()
