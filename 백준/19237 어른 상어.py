import copy

n, m, k = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]

s_dir = [0] + list(map(int, input().split()))

dir = [[]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(m):
    array = []
    for j in range(4):
        array.append(list(map(int, input().split())))
    dir.append(array)


def move(sea):
    global out
    s = copy.deepcopy(sea)
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 0:
                continue
            s_n = s[i][j]
            d = s_dir[s_n]
            x, y = i, j
            what = False
            for p in range(4):
                nd = dir[s_n][d - 1][p]
                nx = x + dx[nd - 1]
                ny = y + dy[nd - 1]
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if smell[nx][ny][1] == 0:
                    if s[nx][ny] == 0:
                        s[nx][ny] = sea[x][y]
                        s[x][y] = 0
                    else:
                        if s[nx][ny] > s[x][y]:
                            s[nx][ny] = sea[x][y]
                        out += 1
                        s[x][y] = 0
                    s_dir[s_n] = nd
                    what = True
                    break
            if what:
                continue

            for p in range(4):
                nd = dir[s_n][d - 1][p]
                nx = x + dx[nd - 1]
                ny = y + dy[nd - 1]
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if smell[nx][ny][1] == s_n:
                    s[nx][ny] = sea[x][y]
                    s[x][y] = 0
                    s_dir[s_n] = nd
                    break
    return s


def s_smell(k):
    for i in range(n):
        for j in range(n):
            if sea[i][j] != 0:
                smell[i][j][0], smell[i][j][1] = k, sea[i][j]


def smell_down():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] == 0:
                continue
            if smell[i][j][0] == 1:
                smell[i][j][0], smell[i][j][1] = 0, 0
            else:
                smell[i][j][0] -= 1


count = 0
out = 0
while True:
    if count >= 1000:
        count = -1
        break
    s_smell(k)
    sea = copy.deepcopy(move(sea))
    count += 1
    if out == m - 1:
        break
    smell_down()

print(count)
