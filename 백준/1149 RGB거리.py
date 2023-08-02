if __name__ == "__main__":
    N = int(input())
    dp = [[0 for _ in range(3)] for _ in range(N)]

    for i in range(N):
        r, g, b = map(int, input().split())
        dp[i][0] = r
        dp[i][1] = g
        dp[i][2] = b

    for i in range(1, N):
        dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])

    print(min(dp[N - 1]))
