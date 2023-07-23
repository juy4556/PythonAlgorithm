from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(space, visited, K):
    q = deque()
    day_night = 1  # 낮(1) 밤(-1)
    q.append([0, 0, K, day_night])
    visited[K][0][0] = 1

    while q:
        x, y, k, dn = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[k][x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                continue
            if space[nx][ny] == 1 and k > 0 and not visited[k - 1][nx][ny] and dn == 1:
                visited[k - 1][nx][ny] = visited[k][x][y] + 1
                q.append([nx, ny, k - 1, -dn])
            elif space[nx][ny] == 0 and not visited[k][nx][ny]:
                visited[k][nx][ny] = visited[k][x][y] + 1
                q.append([nx, ny, k, -dn])
        if dn == -1:
            visited[k][x][y] += 1
            q.append([x, y, k, -dn])

    return -1


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    space = []
    visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]
    result = int(1e9)
    for k in range(K):
        visited[k][0][0] = -1
    for _ in range(N):
        space.append(list(map(int, ' '.join(input()).split())))

    print(bfs(space, visited, K))
