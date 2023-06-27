if __name__ == "__main__":
    N = int(input())
    dp = [0] * 31

    dp[2] = 3
    dp[4] = 11
    for i in range(6, N + 1, 2):
        dp[i] = dp[i - 2] * 3 + sum(dp[:i-2]) * 2 + 2

    print(dp[N])
