import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N, M = map(int, input().split())
    space = []
    for i in range(N):
        space.append(list(map(int, input().split())))
    dp = []
    for i in range(1, M):
        space[0][i] += space[0][i - 1]
    dp.append(space[0][:])

    for i in range(1, N):
        dp.append(space[i][:])
        from_left = dp[i][:]
        from_right = dp[i][:]

        from_left[0] += dp[i - 1][0]
        for j in range(1, M):
            from_left[j] += max(dp[i - 1][j], from_left[j - 1])

        from_right[M - 1] += dp[i - 1][M - 1]
        for j in range(M - 2, -1, -1):
            from_right[j] += max(dp[i - 1][j], from_right[j + 1])

        for j in range(M):
            dp[i][j] = max(from_left[j], from_right[j])

    print(dp[N - 1][M - 1])
