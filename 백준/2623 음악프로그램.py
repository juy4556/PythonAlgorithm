from collections import deque


def topology_sort(graph, indegree):
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    order = []
    while q:
        now = q.popleft()
        order.append(now)
        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)
    return order


if __name__ == "__main__":
    N, M = map(int, input().split())
    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        order = list(map(int, input().split()))
        for i in range(1, len(order)):
            for j in range(i + 1, len(order)):
                graph[order[i]].append(order[j])
                indegree[order[j]] += 1

    result = topology_sort(graph, indegree)
    if len(result) == N:
        for n in result:
            print(n)
    else:
        print(0)
