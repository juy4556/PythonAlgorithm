from collections import defaultdict
import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, parent[a])
    b = find_parent(parent, parent[b])
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    parent = [i for i in range(N + 1)]
    groups = defaultdict(list)
    c = list(map(int, input().split()))
    for _ in range(M):
        a, b = map(int, input().split())
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)

    for i in range(1, N + 1):
        parent[i] = find_parent(parent, parent[i])

    for i in range(1, N + 1):
        if groups[parent[i]]:
            groups[parent[i]][0] += 1
            groups[parent[i]][1] += c[i - 1]
            continue
        groups[parent[i]] = [1, c[i - 1]]

    dp = [[0 for _ in range(K)] for _ in range(len(groups))]

    index = 0
    for a, b in groups.items():
        weight, value = b
        for j in range(1, K):
            if j - weight >= 0:
                dp[index][j] = max(dp[index - 1][j], dp[index - 1][j - weight] + value)
                continue
            dp[index][j] = dp[index - 1][j]
        index += 1

    print(dp[-1][-1])
