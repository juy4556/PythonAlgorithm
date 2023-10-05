import sys

input = sys.stdin.readline
if __name__ == "__main__":
    for _ in range(3):
        N = int(input())
        coins = {}
        total = 0
        for _ in range(N):
            coin, amount = map(int, input().split())
            coins[coin] = amount
            total += coin * amount

        if total & 1:
            print(0)
            continue
        target = total // 2
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for coin in coins.keys():
            for money in range(target, coin - 1, -1):
                if dp[money - coin]:
                    amount = coins[coin]
                    for i in range(amount):
                        if money + coin * i <= target:
                            dp[money + coin * i] = 1

        print(dp[target])
