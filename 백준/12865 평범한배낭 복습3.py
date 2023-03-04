N, K = map(int, input().split())
items = []
for _ in range(N):
    weight, value = map(int, input().split())
    items.append([weight, value])

bag = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= items[i - 1][0]:
            bag[i][j] = max(bag[i - 1][j], items[i - 1][1] + bag[i][j - items[i - 1][0]])
        else:
            bag[i][j] = bag[i - 1][j]

print(bag[N][K])
