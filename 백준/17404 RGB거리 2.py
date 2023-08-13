if __name__ == "__main__":
    N = int(input())
    result = int(1e9)
    rgb = []
    for i in range(1, N + 1):
        rgb.append(list(map(int, input().split())))
    for c in range(3):
        dp = [[int(1e9) for _ in range(3)] for _ in range(N)]
        dp[0][c] = rgb[0][c]
        for i in range(1, N):
            dp[i][0] = rgb[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = rgb[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = rgb[i][2] + min(dp[i - 1][0], dp[i - 1][1])
        for j in range(3):
            if c != j:
                result = min(result, dp[N - 1][j])
    print(result)
