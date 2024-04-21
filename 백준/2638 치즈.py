import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def check_exposed(space):
    q = deque([[0, 0]])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny] or space[nx][ny]:
                continue
            visited[nx][ny] = 1
            q.append([nx, ny])
    return visited


if __name__ == "__main__":
    N, M = map(int, input().split())
    space = []
    for _ in range(N):
        space.append(list(map(int, input().split())))

    time = 0
    while True:
        new_space = space[:]
        all_melted = True
        exposed = check_exposed(space)
        for i in range(N):
            for j in range(M):
                if space[i][j] == 0:
                    continue
                exposed_count = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if nx < 0 or ny < 0 or nx >= N or ny >= M:
                        continue
                    if exposed[nx][ny]:
                        exposed_count += 1
                if exposed_count >= 2:
                    new_space[i][j] = 0
                    all_melted = False

        if all_melted:
            break
        time += 1
        space = new_space[:]

    print(time)
