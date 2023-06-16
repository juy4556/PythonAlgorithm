import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

input = sys.stdin.readline


def plant_bombs():
    for i in range(R):
        for j in range(C):
            if space[i][j] == 0:
                space[i][j] = 1


def explode_bombs():
    for i in range(R):
        for j in range(C):
            if space[i][j] >= 3:
                space[i][j] = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if nx < 0 or ny < 0 or nx > R - 1 or ny > C - 1 or space[nx][ny] >= 3:
                        continue
                    space[nx][ny] = 0


if __name__ == "__main__":
    R, C, N = map(int, input().split())
    space = []

    for _ in range(R):
        space.append(list(' '.join(input().rstrip()).split(' ')))

    for i in range(R):
        for j in range(C):
            if space[i][j] == 'O':
                space[i][j] = 1
            else:
                space[i][j] = 0

    for i in range(R):
        for j in range(C):
            if space[i][j]:
                space[i][j] += 1

    time = 2

    while time <= N:
        if time % 2 == 0:
            plant_bombs()
        else:
            explode_bombs()
        for i in range(R):
            for j in range(C):
                if space[i][j]:
                    space[i][j] += 1
        time += 1

    for i in range(R):
        for j in range(C):
            if space[i][j]:
                print("O", end='')
                continue
            print(".", end='')
        print()
