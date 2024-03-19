from heapq import heappush, heappop
import sys

input = sys.stdin.readline
MAX = 1_000_001


def dijkstra(standard):
    free_count = [MAX for _ in range(N + 1)]
    q = [(0, 1)]
    free_count[1] = 0
    while q:
        count, now = heappop(q)
        if free_count[now] < count:
            continue
        if now == N:
            break
        for node, cost in graph[now]:
            if standard < cost:
                if free_count[node] > count + 1:
                    free_count[node] = count + 1
                    heappush(q, (count + 1, node))
            else:
                if free_count[node] > count:
                    free_count[node] = count
                    heappush(q, (count, node))
    return free_count[N]


if __name__ == "__main__":
    result = MAX
    N, P, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(P):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    left, right = 0, MAX
    while left <= right:
        mid = (left + right) // 2
        if dijkstra(mid) <= K:
            right = mid - 1
            result = mid
        else:
            left = mid + 1

    if result == MAX:
        print(-1)
    else:
        print(result)
