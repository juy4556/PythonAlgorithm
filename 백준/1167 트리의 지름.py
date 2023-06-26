from collections import deque


def bfs(start):
    q = deque([(start, 0)])
    distance = 0
    visited = [0 for _ in range(V + 1)]
    visited[start] = 1
    v = start
    while q:
        node, dist = q.popleft()
        if distance < dist:
            distance = dist
            v = node
        for n, c in nodes[node]:
            if visited[n]:
                continue
            visited[n] = 1
            q.append((n, dist + c))
    return v, distance


if __name__ == "__main__":
    V = int(input())
    nodes = [[] for _ in range(V + 1)]
    for _ in range(V):
        arr = list(map(int, input().split()))
        for i in range(1, len(arr) - 1, 2):
            nodes[arr[0]].append((arr[i], arr[i + 1]))
    node, dist = bfs(1)
    print(bfs(node)[1])
