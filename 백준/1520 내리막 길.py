import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(a, b):
    if a == M - 1 and b == N - 1:
        return 1

    if dp[a][b] != -1:
        return dp[a][b]

    way = 0
    for d in range(4):
        na = a + dx[d]
        nb = b + dy[d]
        if na < 0 or nb < 0 or na > M - 1 or nb > N - 1:
            continue
        if space[a][b] > space[na][nb]:
            way += dfs(na, nb)

    dp[a][b] = way
    return dp[a][b]


if __name__ == "__main__":
    M, N = map(int, input().split())
    space = []
    for _ in range(M):
        space.append(list(map(int, input().split())))
    dp = [[-1 for _ in range(N)] for _ in range(M)]

    print(dfs(0, 0))
