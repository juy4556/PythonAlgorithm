'''
00110
10000
00001
10011
00000
'''
import sys

plus = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]]
cross = [[0, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
input = sys.stdin.readline
N = 5
M = 5
space = [[0, 0, 1, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0]]
result = N * M


def press_button(space, x, y):
    if (x + y) & 1:
        for dx, dy in cross:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                space[nx][ny] ^= 1
    else:
        for dx, dy in plus:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                space[nx][ny] ^= 1


def check_space(space):
    count = 0
    for i in range(N):
        count += space[i].count(1)
        if count:
            return False
    return True


def dfs(pos, space, visited, depth):
    global result
    if check_space(space):
        result = min(result, depth)
        return
    if depth >= result:
        return
    for i in range(0, len(pos)):
        x, y = pos[i]
        if not visited[i] and space[x][y] == 1:
            visited[i] = 1
            press_button(space, x, y)
            dfs(pos, space[:], visited, depth + 1)
            press_button(space, x, y)
            visited[i] = 0


if __name__ == "__main__":
    pos = []
    for i in range(N):
        for j in range(M):
            pos.append((i, j))
    visited = [0 for _ in range(N * M)]

    dfs(pos, space[:], visited, 0)
    print(result)
