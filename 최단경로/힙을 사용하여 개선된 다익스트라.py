# 파이썬의 힙큐는 원소로 튜플을 입력받으면 튜플의 첫 번째 원소를 기준으로 우선순위 큐를 구성한다.
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
# 최단 거리가 가장 짧은 노드를 찾는 과정을 힙을 이용한 우선순위큐로 대체하기 때문에 visited 리스트 필요없음
# visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # dist는 시작 노드로부터의 거리
        if distance[now] < dist: # 우선순위큐를 사용하여 dist를 기준으로 작은 순서로 정렬되기 때문에 시작 노드로부터 현재 노드 까지의 거리가 dist보다 짧다면 이미 앞에서 처리가 된 것 -> continue
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])