from collections import deque

N, M, K = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))
dice = [i for i in range(1, 7)]  # 1: top 2: front 3: right 4: left 5: back 6: bottom
top, back, right, left, front, bottom = 0, 1, 2, 3, 4, 5
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, value):
    q = deque()
    q.append((x, y))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[x][y] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if space[nx][ny] == value:
                    count += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return count * value


def solution():
    d, result = 0, 0
    x, y = 0, 0
    for k in range(K):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            pass
        else:
            d = (d + 2) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        if d == 0:  # 동
            dice[right], dice[bottom], dice[left], dice[top] = dice[top], dice[right], dice[bottom], dice[left]
        elif d == 1:  # 남
            dice[top], dice[back], dice[bottom], dice[front] = dice[back], dice[bottom], dice[front], dice[top]
        elif d == 2:  # 서
            dice[top], dice[left], dice[bottom], dice[right] = dice[right], dice[top], dice[left], dice[bottom]
        elif d == 3:  # 북
            dice[top], dice[front], dice[bottom], dice[back] = dice[front], dice[bottom], dice[back], dice[top]
        result += bfs(nx, ny, space[nx][ny])
        if dice[bottom] > space[nx][ny]:
            d = (d + 1) % 4
        elif dice[bottom] < space[nx][ny]:
            d = (d - 1) % 4
        x, y = nx, ny

    print(result)


solution()
