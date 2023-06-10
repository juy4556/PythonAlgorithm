N = int(input())
triangle = []
for _ in range(N):
    triangle.append(list(map(int, input().split())))

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = triangle[0][0]
for i in range(1, N):
    for j in range(len(triangle[i])):
        if j == 0:
            dp[i][j] = triangle[i][j] + dp[i - 1][j]
        elif j == len(triangle[i]) - 1:
            dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[N - 1]))
