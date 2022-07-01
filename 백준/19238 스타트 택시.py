from collections import deque

N, M, F = map(int, input().split())
space = []
passenger = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(N):
    space.append(list(map(int, input().split())))
taxi_x, taxi_y = map(int, input().split())
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())  # 출발 및 도착 x,y 좌표
    passenger.append([sx - 1, sy - 1, ex - 1, ey - 1])


def find_passenger(x, y):
    global F
    q = deque()
    q.append([x, y])
    dist = [[-1] * N for _ in range(N)]
    dist[x][y] = 0
    while q:
        a, b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1 or space[nx][ny] == 1:
                continue
            if dist[nx][ny] >= 0:
                continue
            dist[nx][ny] = dist[a][b] + 1
            q.append([nx, ny])
    index = len(passenger)
    min_dist = int(1e9)
    passenger.sort(key = lambda k: (k[0], k[1]))
    for i in range(len(passenger)):
        if 0 <= dist[passenger[i][0]][passenger[i][1]] < min_dist:
            min_dist = dist[passenger[i][0]][passenger[i][1]]
            index = i
    F -= min_dist
    return index


def move(index):
    global F
    sx, sy, ex, ey = passenger[index][0], passenger[index][1], passenger[index][2], passenger[index][3]
    dist = [[-1] * N for _ in range(N)]
    dist[sx][sy] = 0
    q = deque()
    q.append([sx, sy])
    flag = False
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1 or space[nx][ny] == 1:
                continue
            if dist[nx][ny] >= 0:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append([nx, ny])
            if nx == ex and ny == ey:
                flag = True
                if F < dist[ex][ey]:
                    flag = False
                else:
                    F += dist[ex][ey]
                return flag
    return flag


def solution():
    a, b = taxi_x - 1, taxi_y - 1
    flag = False
    while True:
        if len(passenger) == 0:
            flag = True
            break
        index = find_passenger(a, b)
        if index == len(passenger) or F <= 0:  # index가 N이면 passenger가 없거나
            break

        if move(index):
            sx, sy, ex, ey = passenger.pop(index)
            a, b = ex, ey
        else:
            break
    if flag:
        print(F)
    else:
        print(-1)


solution()
