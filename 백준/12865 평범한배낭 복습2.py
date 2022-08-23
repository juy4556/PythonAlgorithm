N, K = map(int, input().split())
items = [[0, 0]]
for _ in range(N):
    w, v = map(int, input().split())
    items.append([w, v])

bag = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= items[i][0]:
            bag[i][j] = max(bag[i-1][j], items[i][1] + bag[i - 1][j-items[i][0]])
        else:
            bag[i][j] = bag[i-1][j]

print(bag[N][K])
