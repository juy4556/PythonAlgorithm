import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0 for _ in range(N + 1)]
    dp[1] = 1
    for i in range(2, N + 1):
        for j in range(1, i):
            if A[i - 1] < A[j - 1]:
                dp[i] = max(dp[i], dp[j] + 1)
        if dp[i] == 0:
            dp[i] = 1

    print(max(dp))
