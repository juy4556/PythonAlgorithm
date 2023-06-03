dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def get_age():
    global breeders
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                trees[i][j].sort()
                for k in range(len(trees[i][j])):
                    if trees[i][j][k] <= nutrient[i][j]:
                        nutrient[i][j] -= trees[i][j][k]
                        trees[i][j][k] += 1
                        if trees[i][j][k] % 5 == 0:
                            breeders.append([i, j, k])
                        continue
                    die(i, j, trees[i][j][k:])
                    trees[i][j] = trees[i][j][:k]
                    break


def die(a, b, dead):
    global deads
    deads.append([a, b] + [dead])


def change_nutrient(deads):
    for i in range(len(deads)):
        a, b, dead = deads[i]
        for j in range(len(dead)):
            nutrient[a][b] += dead[j] // 2
    deads.clear()


def breed(breeders):
    for k in range(len(breeders)):
        a, b, c = breeders[k]
        for d in range(8):
            na = a + dx[d]
            nb = b + dy[d]
            if na < 0 or na > N - 1 or nb < 0 or nb > N - 1:
                continue
            trees[na][nb].append(1)
    breeders.clear()


def add_nutrient(nutrient):
    for i in range(N):
        for j in range(N):
            nutrient[i][j] += A[i][j]


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    nutrient = [[5 for _ in range(N)] for _ in range(N)]
    A = []
    trees = [[[] for _ in range(N)] for _ in range(N)]
    deads = []
    breeders = []
    result = 0
    for i in range(N):
        arr = list(map(int, input().split()))
        A.append(arr)

    for _ in range(M):
        x, y, z = map(int, input().split())  # 나무 좌표 및 나이 입력
        trees[x - 1][y - 1].append(z)

    for _ in range(K):
        get_age()
        change_nutrient(deads)
        breed(breeders)
        add_nutrient(nutrient)

    for i in range(N):
        for j in range(N):
            result += len(trees[i][j])

    print(result)
