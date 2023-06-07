import sys

input = sys.stdin.readline

if __name__ == "__main__":
    index = 0
    length = 0
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[] for _ in range(N + 1)]
    dp[1] = [A[0]]

    for i in range(2, N + 1):
        for j in range(1, i):
            if A[i - 1] > A[j - 1]:
                if len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [A[i - 1]]

        if len(dp[i]) == 0:
            dp[i] = [A[i - 1]]

    for i in range(1, N + 1):
        if length < len(dp[i]):
            length = len(dp[i])
            index = i

    print(length)
    print(*dp[index])
