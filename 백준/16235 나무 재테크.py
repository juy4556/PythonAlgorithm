N, M, K = map(int, input().split())
A = []
tree = [[[] for _ in range(N)] for _ in range(N)]
space = [[5] * N for _ in range(N)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)


def spring_summer():
    for i in range(N):
        for j in range(N):
            tree[i][j].sort()
            for t in range(len(tree[i][j])):
                if space[i][j] >= tree[i][j][t]:  # 나무가 자신의 나이만큼 양분을 먹고, 나이가 1증가
                    space[i][j] -= tree[i][j][t]
                    tree[i][j][t] += 1
                else:  # 양분이 나이만큼 없을 땐 즉시 죽음
                    for k in range(t, len(tree[i][j])):
                        space[i][j] += tree[i][j][k] // 2
                    tree[i][j] = tree[i][j][:t]
                    break


def fall():
    for i in range(N):
        for j in range(N):
            for t in range(len(tree[i][j])):
                if tree[i][j][t] % 5 == 0:
                    for d in range(8):
                        new_x = i + dx[d]
                        new_y = j + dy[d]
                        if 0 <= new_x < N and 0 <= new_y < N:
                            tree[new_x][new_y].append(1)


def winter():
    for i in range(N):
        for j in range(N):
            space[i][j] += A[i][j]


def solution():
    result = 0
    for k in range(K):
        spring_summer()
        fall()
        winter()

    for i in range(N):
        for j in range(N):
            result += len(tree[i][j])
    print(result)


solution()
