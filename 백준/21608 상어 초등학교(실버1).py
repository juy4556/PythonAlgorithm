import sys
input = sys.stdin.readline
n = int(input())

student = [[] for _ in range(n**2+1)]
space = [[0] * (n+1) for _ in range(n+1)]
dx = [-1, 0, 1, 0] # 상우하좌
dy = [0, 1, 0, -1]

for _ in range(n**2):
    a, b, c, d, e = map(int, input().split())
    student[a].append([b, c, d, e])
    x = 1
    y = 1
    max_like = -1
    max_empty = -1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if space[i][j] == 0:
                like_count = 0
                empty_count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 1<=nx<=n and 1<=ny<=n:
                        if space[nx][ny] in student[a][0]:
                            like_count += 1
                        if space[nx][ny] == 0:
                            empty_count += 1
                if max_like < like_count or (max_like == like_count and max_empty <empty_count):
                    x, y = i, j
                    max_like = like_count
                    max_empty = empty_count
    space[x][y] = a

satisfied_sum = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 1<=nx<=n and 1<=ny<=n:
                if space[nx][ny] in student[space[i][j]][0]:
                    count += 1
        if count == 1:
            satisfied_sum += 1
        elif count == 2:
            satisfied_sum += 10
        elif count == 3:
            satisfied_sum += 100
        elif count == 4:
            satisfied_sum += 1000

print(satisfied_sum)