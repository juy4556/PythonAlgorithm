import heapq


def bfs(start, costs):
    q = []
    heapq.heappush(q, (0, start))
    costs[start] = 0
    while q:
        cost, now = heapq.heappop(q)

        for n, c in graph[now]:
            if costs[n] > cost + c:
                costs[n] = cost + c
                heapq.heappush(q, (costs[n], n))


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    costs = [int(1e9) for _ in range(N + 1)]
    costs[0] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    bfs(1, costs)
    print(costs[N])
