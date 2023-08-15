import sys

input = sys.stdin.readline


def check_row(target, col):
    for i in range(9):
        if space[i][col] == target:
            return True
    return False


def check_column(target, row):
    for i in range(9):
        if space[row][i] == target:
            return True
    return False


def check_box(target, row, col):
    nr = row // 3 * 3
    nc = col // 3 * 3
    for i in range(nr, nr + 3):
        for j in range(nc, nc + 3):
            if space[i][j] == target:
                return True
    return False


def dfs(n):
    if n == len(blank):
        for i in range(9):
            for j in range(9):
                print(space[i][j], end='')
            print()
        exit()
    x, y = blank[n]
    for num in range(1, 10):
        if check_row(num, y) or check_column(num, x) or check_box(num, x, y):
            continue
        space[x][y] = num
        dfs(n + 1)
        space[x][y] = 0


if __name__ == "__main__":
    space = []
    for _ in range(9):
        space.append(list(map(int, ' '.join(input()).split())))
    filled = [[0 for _ in range(9)] for _ in range(9)]
    blank = []
    for i in range(9):
        for j in range(9):
            if space[i][j] == 0:
                blank.append((i, j))
    dfs(0)
