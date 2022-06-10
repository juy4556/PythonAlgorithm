dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
space = []
clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
visited = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N):
    space.append(list(map(int, input().split())))


def move_cloud(d, s):
    global clouds
    for i in range(len(clouds)):
        clouds[i][0] = clouds[i][0] + dx[d] * s
        clouds[i][1] = clouds[i][1] + dy[d] * s
        clouds[i][0] = clouds[i][0] % N
        clouds[i][1] = clouds[i][1] % N
    for i in range(len(clouds)):
        space[clouds[i][0]][clouds[i][1]] += 1
        visited[clouds[i][0]][clouds[i][1]] = True


def copy_water():
    global visited
    for i in range(len(clouds)):
        count = 0
        x = clouds[i][0]
        y = clouds[i][1]
        for j in range(1, 8, 2):
            new_x = clouds[i][0] + dx[j]
            new_y = clouds[i][1] + dy[j]
            if new_x > N - 1 or new_y > N - 1 or new_x < 0 or new_y < 0:
                continue
            if space[new_x][new_y] >= 1:
                count += 1
        space[x][y] += count


def make_clouds():
    global clouds
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if space[i][j] >= 2 and not visited[i][j]:
                new_clouds.append([i, j])
                space[i][j] -= 2
    clouds = new_clouds


def solution():
    global clouds, visited
    for _ in range(M):
        visited = [[False for _ in range(N)] for _ in range(N)]
        d, s = map(int, input().split())
        move_cloud(d - 1, s)
        copy_water()
        make_clouds()

    result = 0
    for i in range(N):
        for j in range(N):
            result += space[i][j]

    print(result)


solution()
