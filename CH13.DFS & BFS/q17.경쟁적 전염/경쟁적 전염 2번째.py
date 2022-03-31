import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
space = []
for _ in range(n):
    space.append(list(map(int, input().split())))

s, x, y = map(int, input().split())
second = 0
q = deque()


def expansion(v, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
            continue
        if space[nx][ny] == 0:
            space[nx][ny] = v
            q.append((space[nx][ny], (nx, ny)))


virus_count = 0
temp = [] # sort하고 queue에 푸쉬하기 위해 사용
for i in range(n):
    for j in range(n):
        if 1 <= space[i][j] <= k:
            temp.append((space[i][j], (i, j)))
            virus_count += 1

temp.sort(key=lambda x:x[0])

for i in range(len(temp)):
    q.append(temp[i])

while second<s:
    second += 1
    for _ in range(virus_count):
        if q:
            virus, (a, b) = q.popleft()
            expansion(virus, a, b)
        else:
            break

print(space[x-1][y-1])