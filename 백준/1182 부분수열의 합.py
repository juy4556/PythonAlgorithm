import sys

input = sys.stdin.readline
n, s = map(int, input().split())
array = list(map(int, input().split()))
result = 0


def dfs(i, sum):
    global result
    if i > n - 1:
        return
    sum += array[i]
    if (sum == s):
        result += 1
    dfs(i + 1, sum)
    dfs(i + 1, sum - array[i])


dfs(0, 0)
print(result)
