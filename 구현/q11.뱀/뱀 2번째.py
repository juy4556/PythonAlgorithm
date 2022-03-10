import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
k = int(input())
dx = [-1, 0, 1, 0] # 상 우 하 좌 순
dy = [0, 1, 0, -1]
space = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    space[a][b] = 1

l = int(input()) # 뱀의 방향 변환 횟수

turn = deque()
for _ in range(l):
    x, c = input().split()
    turn.append((int(x), c))

staying = deque()
staying.append((1, 1))
direction = 1
times = 0
nx, ny = 1, 1

while staying:
    times += 1
    nx = nx + dx[direction]
    ny = ny + dy[direction]
    if nx < 1 or ny < 1 or nx > n or nx > n:
        break
    if (nx, ny) in staying:
        break
    staying.append((nx, ny))

    if space[nx][ny] == 1:
        staying.appendleft(staying[0])
        space[nx][ny] = 0
    if turn:
        if turn[0][0] == times:
            if turn[0][1] == 'L':
                direction -= 1
                if direction < 0:
                    direction = 3
            elif turn[0][1] == 'D':
                direction += 1
                if direction > 3:
                    direction = 0
            turn.popleft()
    staying.popleft()

print(times)