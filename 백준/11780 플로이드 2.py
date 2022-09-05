n = int(input())
m = int(input())
MAX = int(1e9)
cities = [[MAX for _ in range(n)] for _ in range(n)]
graph = [[0 for _ in range(n)] for _ in range(n)]


def shortestPath(a, b):
    if graph[a][b] == 0:
        return []
    k = graph[a][b]
    return shortestPath(a, k-1) + [k] + shortestPath(k-1, b)


for _ in range(m):
    a, b, c = map(int, input().split())
    if cities[a - 1][b - 1] > c:
        cities[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if cities[i][j] > cities[i][k] + cities[k][j]:
                cities[i][j] = cities[i][k] + cities[k][j]
                graph[i][j] = k + 1
for i in range(n):
    for j in range(n):
        if cities[i][j] == MAX:
            cities[i][j] = 0
        print(cities[i][j], end=' ')
    print()

for i in range(n):
    for j in range(n):
        if cities[i][j] == 0:
            print(0)
            continue
        path = [i+1] + shortestPath(i, j) + [j+1]
        print(len(path), end=' ')
        print(*path)
