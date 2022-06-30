from collections import deque

N = int(input())
space = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
baby_shark = []
result = 0
for _ in range(N):
    space.append(list(map(int, input().split())))


def check_count():
    global result
    eatable = []
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    q.append([baby_shark[0], baby_shark[1]])
    visited[baby_shark[0]][baby_shark[1]] = 0
    while q:
        x, y = q.pop()
        if 0 < space[x][y] < baby_shark[2] and space[x][y] != 9:
            eatable.append([x, y, visited[x][y]])
        for d in range(4):
            new_x = x + dx[d]
            new_y = y + dy[d]
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or space[new_x][new_y] > baby_shark[2]:
                continue
            if visited[new_x][new_y] < 0 or (visited[new_x][new_y] >= 0 and visited[new_x][new_y] > visited[x][y] + 1):
                visited[new_x][new_y] = visited[x][y] + 1
                q.append([new_x, new_y])

    if len(eatable) == 0:
        return False

    elif len(eatable) == 1:
        space[eatable[0][0]][eatable[0][1]] = 0
        result += eatable[0][2]
        space[baby_shark[0]][baby_shark[1]] = 0
        baby_shark[0], baby_shark[1] = eatable[0][0], eatable[0][1]
        space[baby_shark[0]][baby_shark[1]] = 9

    elif len(eatable) > 1:
        min_dist = int(1e9)
        temp = []
        for i in range(len(eatable)):
            if min_dist > eatable[i][2]:
                temp = []
                min_dist = eatable[i][2]
                temp.append([eatable[i][0], eatable[i][1], eatable[i][2]])
            elif min_dist == eatable[i][2]:
                temp.append([eatable[i][0], eatable[i][1], eatable[i][2]])

        if len(temp) > 1:
            temp.sort(key=lambda x: (x[0], x[1]))
        space[temp[0][0]][temp[0][1]] = 0
        space[baby_shark[0]][baby_shark[1]] = 0
        baby_shark[0], baby_shark[1] = temp[0][0], temp[0][1]
        result += min_dist
        space[baby_shark[0]][baby_shark[1]] = 9

    return True


def solution():
    global baby_shark
    eat_count = 0
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                baby_shark = [i, j, 2]  # x,y좌표 및 크기
    while True:
        if not check_count():
            break
        eat_count += 1
        if eat_count == baby_shark[2]:  # 물고기 먹은 수가 아기상어 크기와 같으면 아기상어의 크기를 1증가
            baby_shark[2] += 1
            eat_count = 0

    print(result)


solution()
