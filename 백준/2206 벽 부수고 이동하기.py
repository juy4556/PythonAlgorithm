from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(space, visited):
    visited[0][0][0], visited[1][0][0] = 1, 1
    q = deque([[0, 0, 0]])
    while q:
        x, y, cnt = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                continue
            if space[nx][ny] == 0 and not visited[cnt][nx][ny]:
                visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                q.append([nx, ny, cnt])
            elif space[nx][ny] == 1 and not visited[1][nx][ny] and cnt == 0:
                visited[1][nx][ny] = visited[0][x][y] + 1
                q.append([nx, ny, 1])


if __name__ == "__main__":
    N, M = map(int, input().split())
    space = []
    visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    result = 1000001
    for _ in range(N):
        space.append(list(map(int, ' '.join(input()).split())))

    bfs(space, visited)
    for i in range(2):
        if visited[i][N - 1][M - 1]:
            result = min(result, visited[i][N - 1][M - 1])
    if result < 1000001:
        print(result)
    else:
        print("-1")
