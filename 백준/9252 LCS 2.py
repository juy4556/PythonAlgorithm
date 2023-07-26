if __name__ == "__main__":
    a = input().rstrip()
    b = input().rstrip()
    a_length, b_length = len(a), len(b)
    dp = [[0 for _ in range(b_length + 1)] for _ in range(a_length + 1)]
    result = ""

    for i in range(1, a_length + 1):
        for j in range(1, b_length + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                continue
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    n, m = a_length, b_length
    while n >= 1 and m >= 1:
        if dp[n][m] == dp[n - 1][m]:
            n -= 1
        elif dp[n][m] == dp[n][m - 1]:
            m -= 1
        else:
            result += a[n - 1]
            n -= 1
            m -= 1
    print(dp[a_length][b_length])
    print(result[::-1])
