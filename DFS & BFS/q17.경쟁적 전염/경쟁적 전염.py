import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())  # n은 1이상 200이하, k는 1이상 1000이하

dx = [-1, 0, 1, 0]  # 상우하좌
dy = [0, 1, 0, -1]

space = []
for _ in range(n):
    space.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

q = deque()
temp = []
count = 0
for i in range(n):
    for j in range(n):
        if space[i][j] != 0:
            temp.append((space[i][j], (i, j)))
            count += 1

temp.sort(key=lambda virus: virus[0])
for i in range(len(temp)):
    q.append(temp[i])




def extension(k, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
            continue

        if space[nx][ny] == 0:
            space[nx][ny] = k
            q.append((k, (nx, ny)))


time = 0
while time < s:
    time += 1
    for _ in range(count):
        if q:
            now, (a, b) = q.popleft()
            extension(now, a, b)
        else:
            break


print(space[x-1][y-1])