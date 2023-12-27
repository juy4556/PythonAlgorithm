import sys

input = sys.stdin.readline
if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = set()
    for _ in range(n):
        coins.add(int(input()))
    coins = list(coins)
    n = len(coins)
    dp = [100001 for _ in range(k + 1)]
    for i in range(coins[0], k + 1):
        if i % coins[0] == 0:
            dp[i] = i // coins[0]

    for i in range(1, n):
        if coins[i] > k:
            continue
        for j in range(1, k + 1):
            if j >= coins[i]:
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
                if j % coins[i] == 0:
                    dp[j] = min(dp[j], j // coins[i])

    if dp[k] != 100001:
        print(dp[k])
    else:
        print(-1)
