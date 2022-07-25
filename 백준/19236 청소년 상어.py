import heapq
from collections import defaultdict

space = []
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
q = []
fish = defaultdict(list)
for _ in range(4):
    a1, a2, b1, b2, c1, c2, d1, d2 = map(int, input().split())
    space.append([[a1, a2], [b1, b2], [c1, c2], [d1, d2]])
    heapq.heappush(q, [a1, a2])
shark = [0, 0, space[0][0][1]]  # x, y좌표 및 이동방향
result = space[0][0][0]
space[0][0] = [0, -1]  # (0,0) 좌표 물고기 잡아먹힘 -> 물고기 번호와 방향 0, -1로 초기화


def move_fish():
    for i in range(1, 17):
        print(fish[i])
        if fish[i]:
            x, y, dir = fish[i]
            for _ in range(8):
                nx, ny = x + dx[dir], y + dy[dir]
                if nx < 0 or nx > 3 or ny < 0 or ny > 3 or (nx == shark[0] and ny == shark[1]):
                    dir = (dir + 1) % 8
                    continue
                fish[i] = [nx, ny, dir]  # i번 물고기 새로운 위치 및 이동 방향 초기화
                fish[space[nx][ny][0]] = [x, y, space[nx][ny][1]]  # 새로운 위치에 있던 물고기 정보 초기화
                space[x][y][0], space[nx][ny][0] = space[nx][ny][0], space[x][y][0]
                space[x][y][1], space[nx][ny][1] = space[nx][ny][1], space[x][y][1]
                space[nx][ny][1] = dir
                break


def dfs(N):
    global shark, result
    flag = False
    move_fish()
    for i in range(4):
        for j in range(4):
            print(space[i][j], end= ' ')
        print()
    print("===============")
    x, y, dir = shark[0], shark[1], shark[2]
    temp_shark = shark
    for i in range(1, 4):
        nx, ny = x + i * dx[dir], y + i * dy[dir]
        if nx < 0 or nx > 3 or ny < 0 or ny > 3 or space[nx][ny][0] == 0:
            continue
        flag = True
        temp = space[nx][ny]
        temp_fish = fish[space[nx][ny][0]]
        N += space[nx][ny][0]
        shark[0], shark[1], shark[2] = nx, ny, space[nx][ny][1]
        space[nx][ny] = [0, -1]
        fish[space[nx][ny]] = []
        dfs(N)
        shark = temp_shark
        N -= space[nx][ny][0]
        fish[space[nx][ny]] = temp_fish
        space[nx][ny] = temp
    if not flag:
        result = max(result, N)
        return


def solution():
    for i in range(4):
        for j in range(4):
            fish[space[i][j][0]] = [i, j, space[i][j][1] - 1]  # 각 번호에 해당하는 물고기 위치
    print(fish)
    dfs(result)
    print(result)


solution()
