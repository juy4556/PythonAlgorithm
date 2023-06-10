import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    dp = [[0 for _ in range(2)] for _ in range(N)]
    stairs = []
    result = []
    for _ in range(N):
        stairs.append(int(input()))
    dp[0] = [stairs[0], 0]
    if N > 1:
        dp[1] = [stairs[1], stairs[0] + stairs[1]]
    for i in range(2, N):
        dp[i][0] = stairs[i] + max(dp[i - 2])
        dp[i][1] = stairs[i] + dp[i - 1][0]
    print(max(dp[N - 1]))
