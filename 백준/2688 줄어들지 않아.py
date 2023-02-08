import sys

input = sys.stdin.readline
t = int(input())
dp = [[0] * 64 for _ in range(65)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, 65):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]

for _ in range(t):
    n = int(input())
    print(sum(dp[n]))
