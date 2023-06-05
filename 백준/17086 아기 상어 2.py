import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def bfs(sharks, move):
    for i in range(len(sharks)):
        visited = [[0 for _ in range(M)] for _ in range(N)]
        for j in range(len(sharks)):
            visited[sharks[j][0]][sharks[j][1]] = int(1e9)

        q = deque([sharks[i] + [0]])
        while q:
            x, y, count = q.popleft()
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1 or visited[nx][ny]:
                    continue
                if visited[nx][ny] < count + 1:
                    visited[nx][ny] = count + 1
                    move[nx][ny].append(count + 1)
                    q.append([nx, ny, count + 1])


if __name__ == "__main__":
    N, M = map(int, input().split())
    space = []
    sharks = []
    move = [[[] for _ in range(M)] for _ in range(N)]
    result = 0

    for i in range(N):
        arr = list(map(int, input().split()))
        for j in range(M):
            if arr[j] == 1:
                sharks.append([i, j])
        space.append(arr)

    bfs(sharks, move)

    for i in range(N):
        for j in range(M):
            if move[i][j]:
                result = max(result, min(move[i][j]))
    print(result)
