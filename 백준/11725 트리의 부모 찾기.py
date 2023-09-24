import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def dfs(start):
    for node in graph[start]:
        if not parent[node]:
            parent[node] = start
            dfs(node)


if __name__ == "__main__":
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    parent = [0 for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    parent[1] = 1
    dfs(1)
    for i in range(2, N + 1):
        print(parent[i])
