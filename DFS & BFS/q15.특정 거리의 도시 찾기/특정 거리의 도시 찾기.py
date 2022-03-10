from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
dist = [INF] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def dijkstra(graph, start, k):
    q = deque([start])
    dist[start] = 0
    while q:
        now = q.popleft()
        for node in graph[now]:
            if dist[node] == INF:
                dist[node] = dist[now] + 1
                q.append(node)

    count = 0
    for i in range(1, n+1):
        if dist[i] == k:
            count += 1
            print(i)
    if count == 0:
        print(-1)

dijkstra(graph, x, k)