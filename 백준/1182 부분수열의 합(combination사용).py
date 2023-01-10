import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
array = list(map(int, input().split()))

result = 0
for i in range(1, n + 1):
    c = combinations(array, i)
    for j in c:
        if sum(j) == s:
            result += 1

print(result)
