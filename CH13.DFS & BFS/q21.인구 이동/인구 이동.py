from collections import deque
import sys
input = sys.stdin.readline
n, l, r = map(int, input().split())
country = []
for _ in range(n):
    country.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] # 상우하좌
dy = [0, 1, 0, -1]

def process(x, y, index):
    united = [] # (x,y)와 연결된 나라
    united.append((x,y))
    q = deque()
    q.append((x,y))
    union[x][y] = index
    sum = country[x][y]
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>n-1 or ny>n-1:
                continue
            if l<=abs(country[x][y]-country[nx][ny])<=r and union[nx][ny] == -1:
                q.append((nx,ny))
                union[nx][ny]=index
                sum += country[nx][ny]
                count += 1
                united.append((nx,ny))
    for i, j in united:
        country[i][j] = sum//count

total_count = 0
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index+=1
    if index == n * n:
        break
    total_count += 1


print(total_count)