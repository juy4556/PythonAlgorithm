n, m = map(int, input().split())

x, y, direction = map(int, input().split())

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 방문한 위치 저장 위한 맵 생성하고 0으로 초기화
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1 # 현재 위치 방문

space = []
for i in range(n):
    space.append(list(map(int, input().split())))

# 왼쪽으로 회전 정의
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1 # 가본 공간 카운트, 현재 위치 포함이기 때문에 1로 초기화
turn_count = 0
while 1:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if visited[nx][ny] == 0 and space[nx][ny] == 0:
        x = nx
        y = ny
        count += 1
        visited[nx][ny] = 1
        turn_count = 0
    else:
        turn_count += 1

    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if space[nx][ny] == 0:
            x = nx
            y = ny
            visited[nx][ny] = 1
        else:
            break
        turn_count = 0

print(count)
