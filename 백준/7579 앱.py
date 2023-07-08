if __name__ == "__main__":
    N, M = map(int, input().split())
    m = list(map(int, input().split()))
    c = list(map(int, input().split()))

    dp = [[0 for _ in range(sum(c) + 1)] for _ in range(N + 1)]
    result = sum(c) + 1

    for i in range(1, N+1):
        for j in range(1, sum(c) + 1):
            dp[i][j] = dp[i-1][j]
            if j >= c[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i-1]] + m[i-1])

            if dp[i][j] >= M:
                result = min(result, j)

    print(result)
