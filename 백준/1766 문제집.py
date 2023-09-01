import heapq
import sys

input = sys.stdin.readline


def topology_sort(graph, indegree):
    q = []
    result = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)
        result.append(now)
        for n in graph[now]:
            indegree[n] -= 1
            if indegree[n] == 0:
                heapq.heappush(q, n)
    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        indegree[B] += 1

    print(*topology_sort(graph, indegree))
