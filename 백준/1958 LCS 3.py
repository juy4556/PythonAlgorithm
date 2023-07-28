if __name__ == "__main__":
    a = input().rstrip()
    b = input().rstrip()
    c = input().rstrip()

    a_length, b_length, c_length = len(a), len(b), len(c)
    dp = [[[0 for _ in range(c_length + 1)] for _ in range(b_length + 1)] for _ in range(a_length + 1)]

    for i in range(1, a_length + 1):
        for j in range(1, b_length + 1):
            for k in range(1, c_length + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                    continue
                temp = max(dp[i - 1][j][k], dp[i][j - 1][k])
                temp = max(temp, dp[i][j][k - 1])
                dp[i][j][k] = temp

    print(dp[a_length][b_length][c_length])
