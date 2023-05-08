N, M, K = map(int, input().split())

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
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution():
    a, b = 0, 0
    for m in range(M):
        u, v = map(int, input().split())
        if m == K - 1:
            a, b = u, v
            continue
        union_parent(parent, u, v)
    cnt = 0
    for n in range(N):
        if find_parent(parent, a) == find_parent(parent, n + 1):
            cnt += 1
    result = cnt * (N - cnt)

    print(result)


solution()
