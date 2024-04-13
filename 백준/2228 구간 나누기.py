import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    dp = [[[-3276801, -3276801] for _ in range(M + 1)] for _ in range(N + 1)]
    dp[1][1][1] = arr[0]
    for i in range(2, N + 1):
        dp[i][1][1] = arr[i - 1]
        for j in range(1, M + 1):
            # i번째 선택o, max([i-1][j][1], [i-1][j-1][0])
            dp[i][j][1] = max(dp[i][j][1], arr[i - 1] + max(dp[i - 1][j][1], dp[i - 1][j - 1][0]))
            # i번째 선택x, max([i-1][j])
            dp[i][j][0] = max(dp[i][j][0], max(dp[i - 1][j]))
    print(max(dp[N][M]))
