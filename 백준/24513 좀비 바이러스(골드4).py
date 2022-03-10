from collections import deque

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
space = []
for i in range(n):
    space.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
def bfs(space, x, y, z): # x,y는 좌표 z는 바이러스 번호
    queue = deque()
    queue.append((x, y))
    visited[x][y]=True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == False:
                if space[nx][ny] == 0:
                    space[nx][ny] = z
                    queue.append((nx, ny))
            elif visited[nx][ny]:
                space[nx][ny] = 3

for i in range(n):
    for j in range(m):
        if space[i][j] == 1:
            bfs(space,i,j,1)
        elif space[i][j] == 2:
            bfs(space,i,j,2)
