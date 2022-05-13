N, M = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N)]
array = []
result = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
tmp = []


def solution(x, y):
    global result
    if len(array) == 4:
        result = max(result, sum(array))
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
            visited[nx][ny] = True
            array.append(space[nx][ny])
            solution(nx, ny)
            array.pop()
            visited[nx][ny] = False


def comb(arr, begin, end):
    global array
    global result
    if len(tmp) == 3:
        array += tmp
        result = max(result, sum(array))
        array = array[:1]
        return
    for i in range(begin, end):
        tmp.append(arr[i])
        comb(arr, i + 1, end)
        tmp.pop()


for i in range(N):
    for j in range(M):
        temp = []
        array = [space[i][j]]
        visited[i][j] = True
        solution(i, j)
        array = [space[i][j]]
        for k in range(4):  # ㅗ모양
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                temp.append(space[nx][ny])
        if len(temp) >= 3:
            comb(temp, 0, len(temp))
        visited[i][j] = False
print(result)
