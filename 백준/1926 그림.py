from collections import deque


def bfs(a, b):
    q = deque([[a, b]])
    visited[a][b] = 1
    width = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1 or visited[nx][ny]:
                continue
            if space[nx][ny]:
                visited[nx][ny] = 1
                width += 1
                q.append([nx, ny])
    return width


if __name__ == "__main__":
    n, m = map(int, input().split())
    space = []
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    count = 0
    widest = 0

    for _ in range(n):
        space.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if space[i][j] and not visited[i][j]:
                count += 1
                widest = max(widest, bfs(i, j))

    print(count)
    print(widest)
