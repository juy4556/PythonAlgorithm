from heapq import heappush, heappop
import sys

input = sys.stdin.readline


def topology_sort(dest):
    q = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heappush(q, (D[i - 1], i))
    result = [0] + D[:]

    while q:
        cost, now = heappop(q)
        for node in graph[now]:
            indegree[node] -= 1
            result[node] = max(result[node], cost + D[node - 1])
            if indegree[node] == 0:
                heappush(q, (result[node], node))
                if node == dest:
                    break

    return result[dest]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        D = list(map(int, input().split()))
        graph = [[] for _ in range(N + 1)]
        indegree = [0] * (N + 1)
        for _ in range(K):
            X, Y = map(int, input().split())
            graph[X].append(Y)
            indegree[Y] += 1
        W = int(input())
        print(topology_sort(W))
