import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for term in range(1, N):
        for start in range(N - term):
            dp[start][start + term] = int(1e9)

            for t in range(start, start + term):
                dp[start][start + term] = min(dp[start][start + term],
                                              dp[start][t] + dp[t + 1][start + term] + nums[start][0] * nums[t][1] *
                                              nums[start + term][1])
    print(dp[0][N - 1])
