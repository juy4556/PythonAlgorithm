from collections import deque

N, L, R = map(int, input().split())
countries = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(N):
    countries.append(list(map(int, input().split())))

count = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            union = deque()
            union.append((i, j))
            visited[i][j] = True
            teams = []
            while union:
                x, y = union[0][0], union[0][1]
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if L <= abs(countries[nx][ny] - countries[x][y]) <= R and not visited[nx][ny]:
                            flag = 1
                            union.append((nx, ny))
                            visited[nx][ny] = True
                teams.append(union.popleft())
            summary = 0
            cnt = len(teams)
            for a, b in teams:
                summary += countries[a][b]
            for a, b in teams:
                countries[a][b] = summary // cnt
    if flag == 0:
        break
    count += 1

print(count)
