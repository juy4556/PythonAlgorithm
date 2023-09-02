import math
import sys

input = sys.stdin.readline


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


if __name__ == "__main__":
    n = int(input())
    stars = []
    parent = [i for i in range(n)]
    for _ in range(n):
        stars.append(list(map(float, input().split())))

    dist = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = math.sqrt(abs(stars[i][0] - stars[j][0]) ** 2 + abs(stars[i][1] - stars[j][1]) ** 2)
            dist.append([d, i, j])
    dist.sort()
    result = 0
    for i in range(len(dist)):
        a, b = dist[i][1], dist[i][2]
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += dist[i][0]

    print(round(result, 2))
