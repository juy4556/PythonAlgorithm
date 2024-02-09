import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M, H = map(int, input().split())
    blocks = []
    for i in range(N):
        blocks.append(list(map(int, input().split())))
    dp = [[0 for _ in range(H + 1)] for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        dp[i] = dp[i - 1].copy()
        for block in blocks[i - 1]:
            for j in range(block, H + 1):
                dp[i][j] += dp[i - 1][j - block]
    print(type(dp[N][H]))
    print(dp[N][H])
    print(dp[N][H] % 10007)
