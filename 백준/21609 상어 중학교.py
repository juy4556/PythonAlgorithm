from collections import deque

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, visited, bnum):
    q = deque()
    q.append((x, y))
    num = space[x][y]
    visited[x][y] = bnum
    size, rainbow = 1, 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if space[nx][ny] == num and visited[nx][ny] == 0:
                    size += 1
                    visited[nx][ny] = bnum
                    q.append((nx, ny))
                elif space[nx][ny] == 0 and bnum not in visited[nx][ny]:
                    size += 1
                    rainbow += 1
                    visited[nx][ny].append(bnum)
                    q.append((nx, ny))
    return size, rainbow


def remove_block():
    global score
    count = 0
    for i in range(N):
        for j in range(N):
            if space[i][j] > 0 and visited[i][j] == block[0][4]:
                count += 1
                space[i][j] = -2
            elif space[i][j] == 0 and block[0][4] in visited[i][j]:
                count += 1
                space[i][j] = -2

    score += count * count


def gravity():
    for i in range(N):
        j = N - 1
        while j > 0:
            if space[j][i] == -1:
                j -= 1
                continue
            elif space[j][i] == -2:
                k = j - 1
                while k > -1:
                    if space[k][i] == -1:
                        j = k
                        break
                    elif space[k][i] >= 0:
                        space[k][i], space[j][i] = space[j][i], space[k][i]
                        break
                    k -= 1
            j -= 1

score = 0
while True:
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if space[i][j] == 0:
                visited[i][j] = []

    block_num, block = 1, []
    for i in range(N):
        for j in range(N):
            if space[i][j] > 0 and visited[i][j] == 0:
                size, rn = bfs(i, j, visited, block_num)
                if size > 1:
                    block.append([size, rn, i, j, block_num])
                block_num += 1
    if len(block) == 0:
        break

    block.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    remove_block()
    gravity()
    space = list(map(list, zip(*space)))[::-1]
    gravity()

print(score)
