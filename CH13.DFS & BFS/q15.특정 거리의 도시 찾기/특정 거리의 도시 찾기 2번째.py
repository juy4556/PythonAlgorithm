import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = 1e9
dist = [INF]*(n+1)
dist[x] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(graph, start,k):
    q = deque([start])
    count = 0
    while q:
        now = q.popleft()
        for node in graph[now]:
            if dist[node] == INF:
                dist[node] = dist[now]+1
                q.append(node)

    result = []
    for i in range(1,n+1):
        if dist[i] == k:
            result.append(i)
    if len(result)>0:
        for i in range(len(result)):
            print(result[i])
    else:
        print(-1)

dijkstra(graph,x,k)