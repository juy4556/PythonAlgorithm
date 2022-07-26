import copy
from collections import defaultdict

space = []
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
fish = defaultdict(list)
for _ in range(4):
    a1, a2, b1, b2, c1, c2, d1, d2 = map(int, input().split())
    space.append([[a1, a2 - 1], [b1, b2 - 1], [c1, c2 - 1], [d1, d2 - 1]])
result = 0


def move_fish(sx, sy, board):
    for i in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == i:
                    fx, fy = x, y
                    break
            if fx == -1 and fy == -1:
                continue
            fd = board[fx][fy][1]

            for d in range(8):
                dir = (fd + d) % 8
                nx, ny = x + dx[dir], y + dy[dir]
                if nx < 0 or nx > 3 or ny < 0 or ny > 3 or (nx == sx and ny == sy):
                    continue
                board[fx][fy][0], board[nx][ny][0] = board[nx][ny][0], board[fx][fy][0]
                board[fx][fy][1], board[nx][ny][1] = board[nx][ny][1], dir
                break


def dfs(sx, sy, N, board):
    global result
    N += board[sx][sy][0]
    result = max(result, N)
    board[sx][sy][0] = 0
    move_fish(sx, sy, board)
    sd = board[sx][sy][1]
    for i in range(1, 5):
        nx, ny = sx + i * dx[sd], sy + i * dy[sd]
        if nx < 0 or nx > 3 or ny < 0 or ny > 3 or board[nx][ny][0] <= 0:
            continue
        dfs(nx, ny, N, copy.deepcopy(board))


def solution():
    dfs(0, 0, 0, space)
    print(result)


solution()
