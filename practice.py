N, M, K = map(int, input().split())
A = []
tree = []
die_tree = []
temp = []
space = [[5] * N for _ in range(N)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    x, y, z = map(int, input().split())
    tree.append([z, x - 1, y - 1])


def spring():
    tree.sort()  # 나이가 어린 나무부터 양분을 먹음
    for i in range(len(tree)):
        x, y = tree[i][1], tree[i][2]
        if space[x][y] >= tree[i][0]:  # 나무가 자신의 나이만큼 양분을 먹고, 나이가 1증가
            space[x][y] -= tree[i][0]
            tree[i][0] += 1
        else:  # 양분이 나이만큼 없을 땐 즉시 죽음
            die_tree.append(tree[i])

    for dt in die_tree:
        tree.remove(dt)


def summer():
    while die_tree:
        z, x, y = die_tree.pop()
        value = z // 2
        space[x][y] += value


def fall():
    for i in range(len(tree)):
        if tree[i][0] % 5 == 0:
            x, y = tree[i][1], tree[i][2]
            for j in range(8):
                new_x = x + dx[j]
                new_y = y + dy[j]
                if 0 <= new_x < N and 0 <= new_y < N:
                    tree.append([1, new_x, new_y])


def winter():
    for i in range(N):
        for j in range(N):
            space[i][j] += A[i][j]


def solution():
    for k in range(K):
        spring()
        summer()
        fall()
        winter()
    print(space)
    tree.sort(key = lambda x:(x[1],x[2]))
    print(tree)
    result = len(tree)
    print(result)


solution()
