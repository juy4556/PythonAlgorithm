n = int(input())
m = int(input())
MAX = int(1e9)
cities = [[MAX for _ in range(n)] for _ in range(n)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    cities[start-1][end-1] = min(cities[start-1][end-1], cost)


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            cities[i][j] = min(cities[i][j], cities[i][k]+cities[k][j])

for i in range(n):
    for j in range(n):
        if cities[i][j] == MAX:
            print(0, end=' ')
        else:
            print(cities[i][j], end=' ')
    print()