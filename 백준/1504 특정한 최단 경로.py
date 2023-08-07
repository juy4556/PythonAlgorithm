import heapq
import sys

input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [int(1e9) for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    dist[start] = 0
    visited[start] = 1
    while q:
        cost, now = heapq.heappop(q)
        for c, n in graph[now]:
            if not visited[n]:
                if dist[n] > c + dist[now]:
                    dist[n] = c + dist[now]
                    heapq.heappush(q, (dist[n], n))
    return dist


if __name__ == "__main__":
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    result1, result2 = 0, 0
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append([c, b])
        graph[b].append([c, a])
    v1, v2 = map(int, input().split())
    d1 = dijkstra(1)
    result1 += d1[v1]
    result2 += d1[v2]
    d2 = dijkstra(v1)
    result1 += d2[v2]
    result2 += d2[N]
    d3 = dijkstra(v2)
    result1 += d3[N]
    result2 += d3[v1]

    result = min(result1, result2)
    if result >= int(1e9):
        print(-1)
    else:
        print(result)
