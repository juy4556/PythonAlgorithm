from collections import deque


def bin_search(start, end, points):
    result = 1
    while start <= end:
        mid = (start + end) // 2
        if bfs(mid, points):
            result = mid
            start = mid + 1
            continue
        end = mid - 1
    return result


def bfs(weight, points):
    start_point, end_point = points
    q = deque([start_point])
    visited = [0 for _ in range(N + 1)]
    visited[start_point] = 1
    while q:
        point = q.popleft()
        for p, c in graph[point]:
            if not visited[p] and c >= weight:
                visited[p] = 1
                q.append(p)
    return visited[end_point]


if __name__ == "__main__":
    N, M = map(int, input().split())
    bridges = []
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A].append([B, C])
        graph[B].append([A, C])
    points = list(map(int, input().split()))
    print(bin_search(1, 1000000000, points))
