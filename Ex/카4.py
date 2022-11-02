n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]
result = [5, 3]

import heapq
from collections import defaultdict

INF = int(1e9)
dic = defaultdict(int)
def dijkstra(start, distance, summits):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    temp = set()
    s = []
    while q:
        dist, now_node = heapq.heappop(q)
        if distance[now_node] < dist:
            continue
        for i in graph[now_node]:
            if i[0] in gates: # node가 시작점이면 continue
                continue
            cost = distance[now_node] + i[1]
            if cost < distance[i[0]]: # 시작~ i[0]노드까지의 거리보다 cost가 짧으면 distance 초기화
                distance[i[0]] = cost
                if i[0] in summits:
                    s.append(distance[now_node])
                    s.append(i[1])
                heapq.heappush(q, (cost, i[0]))
    print(start, s)
    # result = INF
    # for summit in summits:
    #     result = min(result, s[summit])
    # print(result)
    #
    # print(min(temp))
    # print(summits)
    # print(distance)
    # for summit in summits:
    #     print(distance[summit])


graph = [[] for _ in range(n + 1)]


def solution(n, paths, gates, summits):
    answer = []
    for path in paths:
        a, b, c = path[0], path[1], path[2]
        graph[a].append((b, c))
        graph[b].append((a, c))

    print(graph)
    for gate in gates:
        distance = [INF] * (n + 1)
        dijkstra(gate, distance, summits)

    return answer


solution(n, paths, gates, summits)
