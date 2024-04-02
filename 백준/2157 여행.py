import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N, M, K = map(int, input().split())
    ways = []
    dp = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]
    graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for _ in range(K):
        a, b, c = map(int, input().split())
        if a >= b:
            continue
        graph[a][b] = max(graph[a][b], c)

    dp[1][1] = 0
    for i in range(2, N + 1):
        for j in range(2, M + 1):
            for k in range(1, i):
                if graph[k][i] and dp[k][j - 1] >= 0:
                    dp[i][j] = max(dp[i][j], graph[k][i] + dp[k][j - 1])
    print(max(dp[N]))
