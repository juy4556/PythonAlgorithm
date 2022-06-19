import copy

R, C, T = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
space = []
for _ in range(R):
    space.append(list(map(int, input().split())))


def diffusion(array, r, c):
    count = 0
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx < 0 or ny < 0 or nx >= R or ny >= C or space[nx][ny] == -1:
            continue
        count += 1
    num = space[r][c] // 5
    array[r][c] -= num * count
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx < 0 or ny < 0 or nx >= R or ny >= C or space[nx][ny] == -1:
            continue
        array[nx][ny] += num


def purification(air_purifier):
    # 반시계빵향 순환
    for i in range(air_purifier, 0, -1):
        space[i][0] = space[i-1][0]

    for i in range(C-1):
        space[0][i] = space[0][i+1]

    for i in range(air_purifier):
        space[i][C - 1] = space[i+1][C - 1]

    for i in range(C-1,0,-1):
        space[air_purifier][i] = space[air_purifier][i-1]

    space[air_purifier][0] = -1
    space[air_purifier][1] = 0

    # 시계방향 순환
    for i in range(air_purifier+1, R-1):
        space[i][0] = space[i+1][0]

    for i in range(C-1):
        space[R-1][i] = space[R-1][i+1]

    for i in range(R-1, air_purifier+1, -1):
        space[i][C-1] = space[i-1][C-1]

    for i in range(C - 1, 1, -1):
        space[air_purifier+1][i] = space[air_purifier+1][i-1]
    space[air_purifier + 1][0] = -1
    space[air_purifier + 1][1] = 0


def solution():
    global space
    air_purifier = 0
    for i in range(R):
        if space[i][0] == -1:
            air_purifier = i
            break
    for t in range(T):
        temp = copy.deepcopy(space)
        for i in range(R):
            for j in range(C):
                if space[i][j] > 0:
                    diffusion(temp, i, j)
        space = temp
        purification(air_purifier)

    result = 0
    for i in range(R):
        for j in range(C):
            if space[i][j] > 0:
                result += space[i][j]

    print(result)


solution()
