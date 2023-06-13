import heapq


def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost:
            continue
        for n, c in arr[node]:
            if distance[n] > distance[node] + c:
                distance[n] = distance[node] + c
                heapq.heappush(q, (distance[n], n))


if __name__ == "__main__":
    N, M, X = map(int, input().split())
    arr = [[] for _ in range(N)]
    distance = [int(1e9)] * N
    result = - 1

    for _ in range(M):
        start, end, time = map(int, input().split())
        arr[start - 1].append([end - 1, time])

    dijkstra(X - 1, distance)
    for i in range(N):
        if i == X - 1:
            continue
        dist = [int(1e9)] * N
        dijkstra(i, dist)
        result = max(result, distance[i] + dist[X - 1])

    print(result)
