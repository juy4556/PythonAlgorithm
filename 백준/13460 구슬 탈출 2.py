from collections import deque

N, M = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(input()))
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()


def move(x, y, dx, dy, c):
    while space[x + dx][y + dy] != '#' and space[x][y] != 'O':  # 다음 위치가 벽이 아니고 현재 위치가 구멍이 아닐 때 move
        x += dx
        y += dy
        c += 1  # 얼마나 움직였는지 count
    return x, y, c


def bfs():
    while q:
        rx, ry, bx, by, time = q.popleft()
        if time > 10:
            print(-1)
            return
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i], 0)
            if space[nbx][nby] == 'O':  # 파란공 구멍 들어갔을 때 continue
                continue
            if space[nrx][nry] == 'O':
                print(time)
                return
            if nrx == nbx and nry == nby:  # 구슬이 같은 위치가 됐을 때 카운트했던 거리가 더 긴 구슬의 위치를 한 칸 이전으로 돌린다.
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, time + 1))
    print(-1)


def solution():
    red, blue = [], []
    for i in range(N):
        for j in range(M):
            if space[i][j] == 'R':
                red = [i, j]
            elif space[i][j] == 'B':
                blue = [i, j]
    q.append((red[0], red[1], blue[0], blue[1], 1))
    visited[red[0]][red[1]][blue[0]][blue[1]] = True
    bfs()


solution()
