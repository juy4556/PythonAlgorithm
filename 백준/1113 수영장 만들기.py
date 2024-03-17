import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
space = []
global_visited = []
result = 0


def bfs(a, b):
    q = deque([[a, b]])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[a][b] = 1
    height = space[a][b]
    min_border_height = 10
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                return 0, visited
            if space[nx][ny] <= height and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])
            if height < space[nx][ny] < min_border_height:
                min_border_height = space[nx][ny]
    return min_border_height, visited


def fill(height, arr):
    global result
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                global_visited[i][j] = 1
                result += height - space[i][j]
                space[i][j] = height


if __name__ == "__main__":
    N, M = map(int, input().split())
    for _ in range(N):
        s = list(map(int, " ".join(input().strip()).split()))
        space.append(s)
    global_visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if not global_visited[i][j]:
                h, arr = bfs(i, j)
                if h > 0:
                    fill(h, arr)
    print(result)
