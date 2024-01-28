import sys

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
space = []
horses = []
horse_space = [[]]
N, K = 4, 4
reverse_dir = {0: 1, 1: 0, 2: 3, 3: 2}


def move_horses(x, y):
    for i in horse_space[x][y]:
        horses[i][0] = x
        horses[i][1] = y


def move_to_white(x, y, nx, ny):
    horse_space[nx][ny] += horse_space[x][y]
    horse_space[x][y] = []
    move_horses(nx, ny)


def move_to_red(x, y, nx, ny):
    horse_space[nx][ny] += horse_space[x][y][::-1]
    horse_space[x][y] = []
    move_horses(nx, ny)


def move_to_blue(x, y, index):
    horses[index][2] = reverse_dir[horses[index][2]]
    nx = x + dx[horses[index][2]]
    ny = y + dy[horses[index][2]]
    if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1 or space[nx][ny] == 2:
        return
    if space[nx][ny] == 0:
        move_to_white(x, y, nx, ny)
    elif space[nx][ny] == 1:
        move_to_red(x, y, nx, ny)


if __name__ == "__main__":
    N, K = map(int, input().split())
    horse_space = [[[] for _ in range(N)] for _ in range(N)]
    turn = 0
    for _ in range(N):
        space.append(list(map(int, input().split())))
    for i in range(K):
        r, c, d = map(int, input().split())
        horses.append([r - 1, c - 1, d - 1])
        horse_space[r - 1][c - 1].append(i)

    while turn < 1000:
        turn += 1
        for i in range(K):
            r, c, d = horses[i]
            if horse_space[r][c][0] != i:
                continue
            nr = r + dx[d]
            nc = c + dy[d]
            if nr < 0 or nc < 0 or nr > N - 1 or nc > N - 1 or space[nr][nc] == 2:
                move_to_blue(r, c, i)
            elif space[nr][nc] == 0:
                move_to_white(r, c, nr, nc)
            elif space[nr][nc] == 1:
                move_to_red(r, c, nr, nc)

        for i in range(N):
            for j in range(N):
                if len(horse_space[i][j]) >= 4:
                    print(turn)
                    exit(0)
    print(-1)
