from collections import deque


def bfs(graph, start):
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[node]:
                if visited[now] == 1:
                    visited[node] = 2
                elif visited[now] == 2:
                    visited[node] = 1
                q.append(node)
            else:
                if visited[node] == visited[now]:
                    return 0
    return 1


if __name__ == "__main__":
    N, M = map(int, input().split())
    visited = [0 for _ in range(N + 1)]
    graph = [[] for _ in range(N + 1)]
    result = 0
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for n in range(1, N+1):
        if not visited[n]:
            result = bfs(graph, n)
            if result == 0:
                break

    print(result)
