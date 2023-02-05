import sys

input = sys.stdin.readline
sys.setrecursionlimit(15000)

n = int(input())
space = []
for _ in range(n):
    space.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]  # 상우하좌
dy = [0, 1, 0, -1]


def dfs(x, y, num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1 or temp[nx][ny] == True:
            continue
        if space[nx][ny] > num:
            temp[nx][ny] = True
            dfs(nx, ny, num)


result = 1
for num in range(max(map(max, space))):
    count = 0
    temp = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if space[i][j] > num and temp[i][j] == False:
                temp[i][j] = True
                dfs(i, j, num)
                count += 1
    if result < count:
        result = count

print(result)
