from collections import defaultdict


def find_added_and_node_count(edges):
    dic = defaultdict(int)
    nodes = set()
    for edge in edges:
        dic[edge[0]] += 1
        nodes.add(edge[0])
        nodes.add(edge[1])
    max_node, max_count = 0, 0
    for k, v in dic.items():
        if max_count < v:
            max_count = v
            max_node = k
    return max_node, len(nodes)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    px = find_parent(parent, x)
    py = find_parent(parent, y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py


def solution(edges):
    answer = [0, 0, 0, 0]
    added_node, node_count = find_added_and_node_count(edges)
    answer[0] = added_node
    parents = [i for i in range(node_count + 1)]

    for edge in edges:
        if edge[0] == added_node:
            continue
        else:
            if find_parent(parents, edge[0]) != find_parent(parents, edge[1]):
                union_parent(parents, edge[0], edge[1])

    for i in range(1, node_count + 1):
        parents[i] = find_parent(parents, i)

    parents_dict = defaultdict(list)
    for i in range(1, node_count + 1):
        if parents_dict.get(parents[i]) is None:
            parents_dict[parents[i]] = [1, 0]
        else:
            parents_dict[parents[i]][0] += 1

    for edge in edges:
        if edge[0] == added_node:
            continue
        else:
            parents_dict[parents[edge[0]]][1] += 1
    for counts in parents_dict.values():
        if counts[0] == counts[1]:
            answer[1] += 1
        elif counts[0] - 1 == counts[1]:
            answer[2] += 1
        else:
            answer[3] += 1
    answer[2] -= 1  # added_node
    return answer


print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
# [2,1,1,0]
print(solution(
    [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],
     [11, 9], [3, 8]]))
# [4,0,1,2]
