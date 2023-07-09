from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def arrange_archer(space, arr, begin):
    global result
    if len(arr) == 3:
        new_space = [[space[i][j] for j in range(M)] for i in range(N)]
        result = max(result, start_game(new_space, arr))
    for i in range(begin, M):
        arr.append(i)
        arrange_archer(space, arr, i + 1)
        arr.pop()


def start_game(space, arr):
    dead = 0
    while True:
        dead += attack(space, arr)
        space = move_enemy(space)
        if check(space):
            return dead


def attack(space, arr):
    enemies = bfs(space, arr)
    for x, y in enemies:
        space[x][y] = 0
    return len(enemies)


def bfs(space, arr):
    enemies = set()
    for num in arr:
        q = deque()
        q.append([N - 1, num])
        visited = [[0 for _ in range(M)] for _ in range(N)]
        visited[N - 1][num] = 1
        while q:
            x, y = q.popleft()
            if visited[x][y] > D:
                break
            if space[x][y] and visited[x][y] <= D:
                enemies.add((x, y))
                break
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1 or visited[nx][ny]:
                    continue
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

    return enemies


def move_enemy(space):
    return [[0 for _ in range(M)]] + space[:N - 1]


def check(space):
    for i in range(N):
        if 1 in space[i]:
            return False
    return True


if __name__ == "__main__":
    N, M, D = map(int, input().split())
    space = []
    result = 0

    for _ in range(N):
        space.append(list(map(int, input().split())))

    arrange_archer(space, [], 0)
    print(result)
