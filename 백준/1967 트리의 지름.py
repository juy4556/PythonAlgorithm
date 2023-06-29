import heapq
import sys

input = sys.stdin.readline


def dijkstra(node_count, start):
    q = []
    heapq.heappush(q, (0, start))
    visited = [0] * (node_count + 1)
    visited[start] = 1
    distance = 0
    far_node = 1
    while q:
        cost, now = heapq.heappop(q)
        if distance < cost:
            distance = cost
            far_node = now
        for n, c in graph[now]:
            if visited[n]:
                continue
            visited[n] = 1
            heapq.heappush(q, (cost + c, n))
    return distance, far_node


if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    dist, node = dijkstra(n, 1)
    print(dijkstra(n, node)[0])
