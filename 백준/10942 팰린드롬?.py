import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split()))
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][i] = 1

    for i in range(1, N + 1):
        for j in range(1, i):
            if num[i - 1] == num[j - 1]:
                if dp[i - 1][j + 1]:
                    dp[i][j] = 1
                elif i - 1 - (j - 1) == 1:
                    dp[i][j] = 1

    M = int(input())
    for _ in range(M):
        S, E = map(int, input().split())
        print(dp[E][S])
