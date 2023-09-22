import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def dfs(node):
    for next in graph[node]:
        if not visited[next]:
            visited[next] = 1
            dfs(next)
            dp[node][0] += dp[next][1]
            dp[node][1] += min(dp[next])


if __name__ == "__main__":
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    dp = [[0, 1] for _ in range(N + 1)]  # 자신이 얼리어답터X,얼리어답터O
    visited = [0 for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[v].append(u)
        graph[u].append(v)

    visited[1] = 1
    dfs(1)
    print(min(dp[1]))
