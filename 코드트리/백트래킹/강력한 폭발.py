explosions = [[[-2, 0], [-1, 0], [1, 0], [2, 0]], [[-1, 0], [1, 0], [0, -1], [0, 1]],
              [[-1, -1], [-1, 1], [1, -1], [1, 1]]]


def check(arr, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                count += 1
    return count


def dfs(space, visited, bombs, k):
    global result, n
    if k == len(bombs):
        count = check(visited, n)
        if result < count:
            result = count
        return

    x, y = bombs[k]
    new_visited = [item[:] for item in visited]
    cnt = len(bombs)
    for i in range(len(explosions)):
        explode_cnt = len(bombs)
        for j in range(4):
            nx = x + explosions[i][j][0]
            ny = y + explosions[i][j][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or space[nx][ny] or new_visited[nx][ny]:
                continue
            new_visited[nx][ny] = 1
            explode_cnt += 1
        dfs(space, new_visited, bombs, k + 1)
        new_visited = [item[:] for item in visited]


if __name__ == "__main__":
    result = -1
    n = int(input())
    space = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    bombs = []

    for i in range(n):
        arr = list(map(int, input().split()))
        space.append(arr)
        for j in range(len(arr)):
            if arr[j] == 1:
                visited[i][j] = 1
                bombs.append((i, j))

    dfs(space, visited, bombs, 0)
    print(result)
