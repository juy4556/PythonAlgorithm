from collections import deque

N, M = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))
comb = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = int(1e9)
visited = [[0] * N for _ in range(N)]
virus = []
q = deque()
wall_count = 0


def check(array):
    count = 0
    for i in range(N):
        count += array[i].count(-1)
    if count == wall_count:
        return True
    return False


def spread_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or space[nx][ny] == 1 or visited[nx][ny] >= 0:
            continue
        visited[nx][ny] = visited[x][y] + 1
        q.append([nx, ny])


def bfs():
    global result, visited, q
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for i in range(M):
        q.append([comb[i][0], comb[i][1]])
        visited[comb[i][0]][comb[i][1]] = 0
    time = 0
    while q:
        x, y = q.popleft()
        spread_virus(x, y)
    for i in range(N):
        for j in range(N):
            if space[i][j] == 2 or space[i][j] == 1:
                continue
            time = max(time, visited[i][j])
    if check(visited):
        result = min(result, time)


def comb_three(array, begin):
    if len(comb) == M:
        bfs()
        return
    for i in range(begin, len(array)):
        comb.append(array[i])
        comb_three(array, i + 1)
        comb.pop()


def solution():
    global wall_count
    for i in range(N):
        for j in range(N):
            if space[i][j] == 2:
                virus.append([i, j])
            elif space[i][j] == 1:
                wall_count += 1

    comb_three(virus, 0)
    if result > N:
        print(-1)
    else:
        print(result)


solution()
