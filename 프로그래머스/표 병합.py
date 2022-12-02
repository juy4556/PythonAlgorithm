space = [[0 for _ in range(51)] for _ in range(51)]
parent = [[(i, j) for j in range(51)] for i in range(51)]


def find_parent(parent, x):
    if parent[x[0]][x[1]] != (x[0], x[1]):
        parent[x[0]][x[1]] = find_parent(parent, parent[x[0]][x[1]])
    return parent[x[0]][x[1]]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return
    parent[b[0]][b[1]] = a
    if space[a[0]][a[1]] != 0:
        update2(a[0], a[1], space[a[0]][a[1]])
    else:
        update2(a[0], a[1], space[b[0]][b[1]])


def update1(origin, new):
    for i in range(1, 51):
        for j in range(1, 51):
            a, b = find_parent(parent, (i, j))
            if space[a][b] == origin:
                update2(a, b, new)


def update2(x, y, value):
    a, b = find_parent(parent, (x, y))
    for i in range(1, 51):
        for j in range(1, 51):
            if find_parent(parent, (i, j)) == (a, b):
                space[i][j] = value


def unmerge(x, y):
    a, b = find_parent(parent, (x, y))
    temp = space[a][b]
    for i in range(1, 51):
        for j in range(1, 51):
            if find_parent(parent, (i, j)) == (a, b):
                parent[i][j] = (i, j)
                space[i][j] = 0
    space[x][y] = temp


def print_value(answer, x, y):
    a, b = find_parent(parent, (x, y))
    if space[a][b] == 0:
        answer.append("EMPTY")
        return
    answer.append(space[a][b])


def solution(commands):
    answer = []
    for i in range(len(commands)):
        command = list(commands[i].split())
        if command[0] == "UPDATE":
            if len(command) == 3:
                update1(command[1], command[2])
            elif len(command) == 4:
                update2(int(command[1]), int(command[2]), command[3])

        elif command[0] == "MERGE":
            command[1:5] = map(int, command[1:5])
            union_parent(parent, (command[1], command[2]), (command[3], command[4]))

        elif command[0] == "UNMERGE":
            unmerge(int(command[1]), int(command[2]))

        elif command[0] == "PRINT":
            print_value(answer, int(command[1]), int(command[2]))
    # for i in range(5):
    #     for j in range(5):
    #         print(parent[i][j], end = ' ')
    #     print()
    # for i in range(5):
    #     for j in range(5):
    #         a, b = find_parent(parent, (i,j))
    #         print(space[a][b], end = ' ')
    #     print()
    return answer


print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice",
                "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant",
                "UPDATE 4 1 pasta",
                "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik",
                "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))

print(solution(
    ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1",
     "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))

print(solution(
    ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4",
     "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))
