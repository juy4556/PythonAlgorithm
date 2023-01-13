from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0 for _ in range(N + 1)]
visited2 = [0 for _ in range(N + 1)]


def dfs(v):
    visited2[v] = 1
    print(v, end=" ")
    for i in range(1, N + 1):
        if visited2[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if visited[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited[i] = 1


dfs(V)
print()
bfs(V)
