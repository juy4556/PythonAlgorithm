N = int(input())
S = []
for i in range(N):
    num = int(input())
    S.append(num)
result = 0
max_num = max(S)
dp = [[0 for _ in range(max_num + 1)] for _ in range(N + 1)]
for i in range(1, len(S) + 1):
    dp[i][S[i - 1]] += 1


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(1, N + 1):
    for j in range(1, max_num + 1):
        dp[i][j] += dp[i - 1][j]
        dp[i][j] %= 10000003
        GCD = gcd(S[i - 1], j)
        dp[i][GCD] += dp[i - 1][j]
        dp[i][GCD] %= 10000003
print(dp[N][1])
