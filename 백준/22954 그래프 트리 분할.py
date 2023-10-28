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
    N, M = map(int, input().split())
    graph = [set() for _ in range(N + 1)]
    edges = []
    parent = [i for i in range(N + 1)]
    parents = set()
    group1 = set()
    group2 = set()
    edges1 = []
    edges2 = []
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
        edges.append((u, v))
        if find_parent(parent, u) == find_parent(parent, v):
            # 사이클 발생하면 pass
            continue
        union_parent(parent, u, v)

    if N <= 2:
        print(-1)
        exit()

    for i in range(1, N + 1):
        parent[i] = find_parent(parent, parent[i])
        parents.add(parent[i])

    # For making two groups, we have to connect but cannot in this problem
    if len(parents) == 2:
        parents = list(parents)
        for i in range(1, N + 1):
            if parent[i] == parents[0]:
                group1.add(i)
            else:
                group2.add(i)
        if len(group1) == len(group2):
            print(-1)
            exit()

        parent = [i for i in range(N + 1)]
        for i in range(M):
            u, v = edges[i]
            if find_parent(parent, u) == find_parent(parent, v):
                # cycle 생김
                continue
            union_parent(parent, u, v)
            if u in group1 and v in group1:
                edges1.append(i + 1)
            elif u in group2 and v in group2:
                edges2.append(i + 1)

    elif len(parents) == 1:
        # find_least_connection
        min_connect = 100001
        least_node = 0
        parent = [i for i in range(N + 1)]
        for i in range(1, N + 1):
            if len(graph[i]) < min_connect:
                min_connect = len(graph[i])
                least_node = i

        group1 = set(i for i in range(1, N + 1))
        group1.remove(least_node)
        group2.add(least_node)
        for i in range(M):
            if least_node in edges[i]:
                continue
            u, v = edges[i]
            if find_parent(parent, u) == find_parent(parent, v):
                # cycle 생김
                continue
            union_parent(parent, u, v)
            edges1.append(i + 1)
    else:
        print(-1)
        exit()

    print(len(group1), len(group2))
    print(*group1)
    print(*edges1)
    print(*group2)
    print(*edges2)
