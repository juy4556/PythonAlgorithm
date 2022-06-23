N = int(input())
space = []
comb = []
summary = [0] * 5
result = int(1e9)
for _ in range(N):
    space.append(list(map(int, input().split())))


def check(array, lines):
    global result
    d1, d2, x, y = array[0], array[1], array[2] - 1, array[3] - 1
    summary = [0] * 5
    for i in range(N):
        for j in range(N):
            if 0 <= i < x + d1 and 0 <= j <= y and [i, j] not in lines[0]:
                summary[0] += space[i][j]
            elif 0 <= i <= x + d2 and y < j <= N - 1 and [i, j] not in lines[1]:
                summary[1] += space[i][j]
            elif x + d1 <= i <= N - 1 and 0 <= j < y - d1 + d2 and [i, j] not in lines[2]:
                summary[2] += space[i][j]
            elif x + d2 < i <= N - 1 and y - d1 + d2 <= j <= N - 1 and [i, j] not in lines[3]:
                summary[3] += space[i][j]
            else:
                summary[4] += space[i][j]
    print(summary, sum(summary), x, y, d1, d2)
    if max(summary) - min(summary) == 15:
        print(111111111111111111111111)
    result = min(result, max(summary) - min(summary))


def dfs():
    if len(comb) == 4:
        d1, d2, x, y = comb[0], comb[1], comb[2] - 1, comb[3] - 1
        if 1 <= x < d1 + d2 + x <= N:
            if 1 <= y - d1 < y < y + d2 <= N:
                lines = [[] for _ in range(4)]
                for i in range(d1+1):
                    for j in range(d2+1):
                        lines[0].append([x + i, y - i])
                        lines[1].append([x + j, y + j])
                        lines[2].append([x + d1 + j, y - d1 + j])
                        lines[3].append([x + d2 + d1, y + d2 - d1])
                print(lines)
                check(comb, lines)
        return
    for i in range(1, N + 1):
        comb.append(i)
        dfs()
        comb.pop()


def solution():
    dfs()
    print(result)


solution()
