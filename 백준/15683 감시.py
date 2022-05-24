import copy

N, M = map(int, input().split())
space = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cctv = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]


def fill(arr, mm, x, y):
    for m in mm:
        nx, ny = x, y
        while True:
            nx += dx[m]
            ny += dy[m]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if arr[nx][ny] == 6:
                break
            elif arr[nx][ny] == 0:
                arr[nx][ny] = 7


result = 100


def dfs(depth, arr):
    global result
    if depth == len(cctv):
        count = 0
        for i in range(N):
            count += arr[i].count(0)
        result = min(result, count)
        return
    cctv_num, x, y = cctv[depth]
    temp = copy.deepcopy(arr)
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth + 1, temp)
        temp = copy.deepcopy(arr)


def solution():
    for i in range(N):
        space.append(list(map(int, input().split())))
        for j in range(M):
            if 1 <= space[i][j] <= 5:
                cctv.append([space[i][j], i, j])
    dfs(0, space)
    print(result)

solution()