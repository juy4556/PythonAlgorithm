N = int(input())

planet = []
for i in range(N):
    x, y, z = map(int, input().split())
    planet.append([x, y, z, i+1])

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def init(edges):
    for pos in range(3):
        planet.sort(key=lambda p: p[pos])
        a = planet[0][3]
        for i in range(1,N):
            b = planet[i][3]
            edges.append((abs(planet[i][pos]-planet[i-1][pos]), a, b))
            a = b
    edges.sort()


def solution():
    edges = []
    init(edges)
    result = 0
    for i in range(len(edges)):
        cost, a, b = edges[i]
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    print(result)


solution()
