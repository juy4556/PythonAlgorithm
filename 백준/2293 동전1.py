import sys

input = sys.stdin.readline
if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    dp = [0] * (k + 1)
    for i in range(n):
        c = int(input())
        coins.append(c)

    dp[0] = 1
    for c in coins:
        for i in range(c, k + 1):
            dp[i] += dp[i - c]
    print(dp[k])
