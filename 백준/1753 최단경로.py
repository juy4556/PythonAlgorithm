import heapq

V, E = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(V + 1)]
K = int(input())
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dist = [INF] * (V + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        distance, now = heapq.heappop(q)
        for node in graph[now]:
            cost = dist[now] + node[1]
            if cost < dist[node[0]]:
                dist[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


dijkstra(K)
for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
        continue
    print(dist[i])
