from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
horse_x = [-2, -2, -1, 1, 2, 2, 1, -1]
horse_y = [-1, 1, 2, 2, 1, -1, -2, -2]


def bfs(horse_count):
    q = deque()
    visited = [[[0] * (horse_count + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][horse_count] = 1
    q.append([0, 0, horse_count])
    while q:
        x, y, k = q.popleft()
        if x == H - 1 and y == W - 1:
            print(visited)
            return visited[x][y][k] - 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx > H - 1 or ny > W - 1 or space[nx][ny] or visited[nx][ny][k]:
                continue
            visited[nx][ny][k] = visited[x][y][k] + 1
            q.append([nx, ny, k])

        if k > 0:
            for d in range(8):
                nx = x + horse_x[d]
                ny = y + horse_y[d]
                if nx < 0 or ny < 0 or nx > H - 1 or ny > W - 1 or space[nx][ny] or visited[nx][ny][k - 1]:
                    continue
                visited[nx][ny][k - 1] = visited[x][y][k] + 1
                q.append([nx, ny, k - 1])
    return -1


if __name__ == "__main__":
    K = int(input())
    W, H = map(int, input().split())
    space = []
    for _ in range(H):
        space.append(list(map(int, input().split())))

    print(bfs(K))
