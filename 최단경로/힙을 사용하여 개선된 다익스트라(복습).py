import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
n, e = map(int, input().split()) # input node & edge
start = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(e):
    a, b, c = map(int, input().split()) # a는 출발노드 ,b는 도착노드, c는 비용
    graph[a].append((b, c))

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

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])