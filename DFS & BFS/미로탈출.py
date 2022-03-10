from collections import deque

n, m = map(int, input().split())  # n(세로),m(가로)은 4이상 200이하

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

monster = []  # 0은 괴물 존재, 1은 괴물 X
for i in range(n):
    monster.append(list(map(int, input())))


def bfs(monster, x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if monster[nx][ny] == 0:  # monster 존재 할 경우 패스
                continue
            if monster[nx][ny] == 1:
                monster[nx][ny] = monster[x][y] + 1
                queue.append((nx, ny))
    return monster[n - 1][m - 1]


print(bfs(monster, 0, 0))
