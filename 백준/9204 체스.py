import sys
from collections import deque

input = sys.stdin.readline
move = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
visited = [[0 for _ in range(8)] for _ in range(8)]


def check(X, Y):
    return (abs(X[0] - Y[0]) + abs(X[1] - Y[1])) % 2


def bfs(X, Y):
    q = deque([[X[0], X[1]]])
    visited[X[0]][X[1]] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += move[i][0]
                ny += move[i][1]
                if nx < 0 or ny < 0 or nx > 7 or ny > 7 or visited[nx][ny]:
                    break
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if [nx, ny] == Y:
                    return [x, y]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        x1, y1, x2, y2 = input().split()
        X = [8 - int(y1), ord(x1) - 65]
        Y = [8 - int(y2), ord(x2) - 65]
        if check(X, Y):
            print("Impossible")
            continue
        visited = [[0 for _ in range(8)] for _ in range(8)]
        broker = bfs(X, Y)

        print(visited[Y[0]][Y[1]] - 1, end=" ")

        if broker:
            print(chr(65 + X[1]), 8 - X[0], end=" ")
            if broker != X:
                print(chr(65 + broker[1]), 8 - broker[0], end=" ")
            print(chr(65 + Y[1]), 8 - Y[0])
        else:
            print(chr(65 + X[1]), 8 - X[0])
