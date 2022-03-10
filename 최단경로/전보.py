import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now_node = heapq.heappop(q)
        if distance[now_node] < dist:
            continue
        for i in graph[now_node]:
            cost = distance[now_node] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)
count = 0
max = 0
for i in range(1, m+1):
    if distance[i] != INF:
        count += 1
        if max<distance[i]:
            max=distance[i]

print(count, end=' ')
print(max)