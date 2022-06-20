import copy
from collections import deque

N, M = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))
comb = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = int(1e9)
visited = [[False] * N for _ in range(N)]
flag = False
q = deque()
new_q = deque()


def check(array):
    for i in range(N):
        print(array[i])

    for i in range(N):
        if array[i].count(0) > 0:
            return False
    return True


def spread_virus(temp, x, y):
    global flag, q
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or temp[nx][ny] == 1:
            continue
        temp[nx][ny] = 3
        new_q.append([nx, ny])
        flag = True
    return temp


def comb_three(array, begin):
    global result, visited, flag, q, new_q
    if len(comb) == M:
        q = deque()
        new_q = deque()
        temp = copy.deepcopy(space)
        visited = [[False] * N for _ in range(N)]
        for i in range(M):
            new_q.append([comb[i][0], comb[i][1]])
            temp[comb[i][0]][comb[i][1]] = 3
        time = 0
        flag = False

        for t in range(N):
            q = new_q
            while q:
                if check(temp):
                    break
                print(q)
                x, y = q.popleft()
                if not visited[x][y]:
                    # print(x, y)
                    visited[x][y] = True
                    temp = spread_virus(temp, x, y)
            if flag:
                time += 1
            else:
                break
            result = min(result, time)
            print(result)
        # result = min(result, time)
        return

    for i in range(begin, len(array)):
        comb.append(array[i])
        comb_three(array, i + 1)
        comb.pop()


def solution():
    virus = []
    for i in range(N):
        for j in range(N):
            if space[i][j] == 2:
                virus.append([i, j])

    comb_three(virus, 0)

    if result > N:
        print(-1)
    else:
        print(result)


solution()
