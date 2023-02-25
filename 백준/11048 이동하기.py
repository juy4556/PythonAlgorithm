N, M = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        a, b, c = 0, 0, 0
        if i > 0 and space[i - 1][j]:
            a = space[i - 1][j]
        if j > 0 and space[i][j - 1]:
            b = space[i][j - 1]
        if i > 0 and j > 0 and space[i - 1][j - 1]:
            c = space[i - 1][j - 1]
        tmp = max(a, b)
        maximum = max(tmp, c)
        space[i][j] = space[i][j] + maximum

print(space[N - 1][M - 1])
