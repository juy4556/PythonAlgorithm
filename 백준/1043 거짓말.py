def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, parent[a])
    b = find_parent(parent, parent[b])
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    N, M = map(int, input().split())
    parent = [i for i in range(N + 1)]
    people = list(map(int, input().split()))
    know_true = set(people[1:])
    parties = []
    for i in range(1, people[0] + 1):
        parent[people[i]] = 0

    for _ in range(M):
        members = list(map(int, input().split()))
        parties.append(members[1:])

        for i in range(1, members[0]):
            union_parent(parent, members[i], members[i + 1])

    for i in range(1, N + 1):
        parent[i] = find_parent(parent, i)
        if parent[i] == 0:  # 0이면 진실 아는 것
            know_true.add(i)

    count = M
    for i in range(M):
        for j in range(len(parties[i])):
            if parties[i][j] in know_true:
                count -= 1
                break

    print(count)
