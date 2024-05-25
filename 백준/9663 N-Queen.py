import sys

input = sys.stdin.readline


def dfs(n, row, cols, left, right):
    global result
    if row == n:
        result += 1
        return

    avail_cols = ~(left | cols | right) & ((1 << n) - 1)
    while avail_cols:
        avail_col = avail_cols & -avail_cols
        avail_cols -= avail_col
        dfs(N, row + 1, cols | avail_col, (left | avail_col) << 1, (right | avail_col) >> 1)


if __name__ == "__main__":
    N = int(input())
    result = 0
    dfs(N, 0, 0, 0, 0)
    print(result)
