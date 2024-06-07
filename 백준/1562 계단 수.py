import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    dp = [[[0 for _ in range((1 << 10))] for _ in range(10)] for _ in range(N + 1)]
    MOD = int(1e9)
    result = 0
    for i in range(1, 10):
        dp[1][i][1 << i] = 1

    for i in range(2, N + 1):
        for j in range(10):
            for k in range(1024):
                bits = (1 << j) | k
                if j > 0 and dp[i - 1][j - 1][k]:
                    dp[i][j][bits] += dp[i - 1][j - 1][k]
                if j < 9 and dp[i - 1][j + 1][k]:
                    dp[i][j][bits] += dp[i - 1][j + 1][k]
                dp[i][j][bits] %= MOD

    for last_num in range(10):
        result += dp[N][last_num][1023]
        result %= MOD
    print(result)
