'''
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))

result = 1e9
x, y = 0, 0
for a, b in list(combinations(liquid,2)):
    if result > abs(a+b):
        result = abs(a+b)
        x, y = a, b

print(x, y)
'''

import sys

input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))

start, end = 0, n - 1
x, y = 0, n - 1
result = abs(liquid[start] + liquid[end])
while start < end:
    sum = liquid[start] + liquid[end]
    if result > abs(sum):
        result = abs(liquid[start] + liquid[end])
        x, y = start, end

    if sum < 0:
        start += 1
    elif sum > 0:
        end -= 1
    else:
        break

print(liquid[x], liquid[y])
