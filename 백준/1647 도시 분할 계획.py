def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]


if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = []
    parent = [i for i in range(N + 1)]
    result = 0
    max_cost = 0
    for _ in range(M):
        A, B, C = map(int, input().split())
        edges.append([C, A, B])
    edges.sort()

    for c, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            result += c
            union_parent(parent, a, b)
            max_cost = c
    print(result-max_cost)
