# 각 주식은 최대 한 개만 구매 가능
money = int(input())
N = int(input())
stocks = [[]]
for i in range(N):
    value, price = map(int, input().split())
    stocks.append([value, price])

dp = [[0 for _ in range(money + 1)] for _ in range(money + 1)]


def solution():
    for i in range(1, N + 1):
        for j in range(1, money + 1):
            if j >= stocks[i][1]:
                dp[i][j] = max(dp[i - 1][j], stocks[i][0] + dp[i - 1][j - stocks[i][1]])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[N][money])


solution()
