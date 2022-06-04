N, M = map(int, input().split())
space = []
homes = []
chickens = []
for _ in range(N):
    space.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if space[i][j] == 1:
            homes.append([i + 1, j + 1])
        elif space[i][j] == 2:
            chickens.append([i + 1, j + 1])

result = int(1e9)

c = []


def dfs(begin):
    global result
    if len(c) == M:
        temp = 0
        for h1, h2 in homes:
            tmp = int(1e9)
            for c1, c2 in c:
                tmp = min(tmp, abs((c1 - h1))+abs((c2-h2)))
            temp += tmp
        result = min(result, temp)
        return
    for i in range(begin, len(chickens)):
        c.append(chickens[i])
        dfs(i + 1)
        c.pop()


dfs(0)
print(result)
