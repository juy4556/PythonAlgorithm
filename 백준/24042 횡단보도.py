import sys
import heapq as hq

input = sys.stdin.readline


def bfs(start):
    costs[start] = 0
    visited[start] = 1
    q = []
    hq.heappush(q, (0, start))
    while q:
        cost, now = hq.heappop(q)
        if visited[N]:
            break
        visited[now] = 1
        for c, n in graph[now]:
            time = c - cost % M
            if time < 0:
                time += M
            if not visited[n] and costs[n] > cost + time:
                costs[n] = cost + time
                hq.heappush(q, (cost + time, n))


if __name__ == "__main__":
    N, M = map(int, input().split())
    costs = [int(1e12) for _ in range(N + 1)]
    time = 0
    graph = [[] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    for time in range(1, M + 1):
        a, b = map(int, input().split())
        graph[a].append((time, b))
        graph[b].append((time, a))

    bfs(1)
    print(costs[N])
