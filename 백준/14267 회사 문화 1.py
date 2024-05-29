import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(cur, weight, visited):
    if dp[cur]:
        return
    visited[cur] = 1
    weight += praise_amount[cur]
    dp[cur] += weight
    for node in parents[cur]:
        if not visited[node]:
            dfs(node, weight, visited)


if __name__ == "__main__":
    n, m = map(int, input().split())
    praise = list(map(int, input().split()))
    dp = [0] * (n + 1)
    visited = [0] * (n + 1)
    parents = [[] for _ in range(n + 1)]
    for i in range(1, n):
        parents[praise[i]].append(i + 1)

    praise_amount = [0] * (n + 1)
    for _ in range(m):
        i, w = map(int, input().split())
        praise_amount[i] += w

    dfs(1, 0, visited)
    print(*dp[1:])
