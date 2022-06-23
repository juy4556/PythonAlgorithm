N = int(input())
space = []
comb = []
summary = [0] * 5
result = int(1e9)
for _ in range(N):
    space.append(list(map(int, input().split())))
visited = [[0] * N for _ in range(N)]


def check(array):
    global result
    d1, d2, x, y = array[0], array[1], array[2] - 1, array[3] - 1
    summary = [0] * 5
    for i in range(N):
        for j in range(N):
            if 0 <= i < x + d1 and 0 <= j <= y and not visited[i][j]:
                summary[0] += space[i][j]
            elif 0 <= i <= x + d2 and y < j <= N - 1 and not visited[i][j]:
                summary[1] += space[i][j]
            elif x + d1 <= i <= N - 1 and 0 <= j < y - d1 + d2 and not visited[i][j]:
                summary[2] += space[i][j]
            elif x + d2 < i <= N - 1 and y - d1 + d2 <= j <= N - 1 and not visited[i][j]:
                summary[3] += space[i][j]
            else:
                summary[4] += space[i][j]
    result = min(result, max(summary) - min(summary))


def dfs():
    global visited
    if len(comb) == 4:
        visited = [[0] * N for _ in range(N)]
        d1, d2, x, y = comb[0], comb[1], comb[2] - 1, comb[3] - 1
        if 0 <= x < d1 + d2 + x <= N - 1:
            if 0 <= y - d1 < y < y + d2 <= N - 1:
                for i in range(d1 + 1):
                    visited[x + i][y - i] = 1
                    visited[x + d2 + i][y + d2 - i] = 1
                for j in range(d2 + 1):
                    visited[x + j][y + j] = 1
                    visited[x + d1 + j][y - d1 + j] = 1
                for i in range(len(visited)):
                    if visited[i].count(1) > 1:
                        for j in range(visited[i].index(1) + 1, N):
                            if visited[i][j] == 1:
                                break
                            visited[i][j] = 1
                check(comb)
        return
    for i in range(1, N + 1):
        comb.append(i)
        dfs()
        comb.pop()


def solution():
    dfs()
    print(result)


solution()
