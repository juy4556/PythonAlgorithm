if __name__ == "__main__":
    N, K = map(int, input().split())
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    items = []
    for _ in range(N):
        items.append(list(map(int, input().split())))

    for i in range(1, N + 1):
        weight, value = items[i - 1]
        for j in range(1, K + 1):
            if j < weight:
                dp[i][j] = dp[i-1][j]
                continue
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

    print(dp[N][K])
