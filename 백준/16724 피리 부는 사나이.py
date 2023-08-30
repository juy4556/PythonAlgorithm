import sys

input = sys.stdin.readline


def dfs(x, y, n, arr):
    global cycle
    arr.append((x, y))
    visited[x][y] = n
    nx, ny = x, y
    if space[x][y] == 'U':
        nx -= 1
    elif space[x][y] == 'D':
        nx += 1
    elif space[x][y] == 'L':
        ny -= 1
    elif space[x][y] == 'R':
        ny += 1

    if not visited[nx][ny]:
        dfs(nx, ny, n, arr)
    else:
        if visited[nx][ny] == n:
            cycle += 1
        elif visited[nx][ny] < n:
            for a, b in arr:
                visited[a][b] = visited[nx][ny]
        return


if __name__ == "__main__":
    N, M = map(int, input().split())
    space = []
    for _ in range(N):
        space.append(input().rstrip())
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cycle = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                dfs(i, j, cycle + 1, [])

    print(cycle)
