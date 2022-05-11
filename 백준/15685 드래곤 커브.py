generations = [[0],
               [0, 1],
               [0, 1, 2, 1],
               [0, 1, 2, 1, 2, 3, 2, 1]]
space = set()


def generation():
    for i in range(4, 11):
        generations.append(list(generations[i - 1]))
        length = len(generations[i])
        for j in range(length // 2):
            generations[i].append((generations[i][j] + 2) % 4)
        for k in range(length // 2, length):
            generations[i].append(generations[i][k] % 4)


def move_rotate(x, y, d, g):
    space.add((x, y))
    for i in generations[g]:
        if (i + d) % 4 == 0:
            x += 1
        elif (i + d) % 4 == 1:
            y -= 1
        elif (i + d) % 4 == 2:
            x -= 1
        elif (i + d) % 4 == 3:
            y += 1
        space.add((x, y))


def count_square():
    count = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if (i - 1, j - 1) in space and (i, j - 1) in space and (i - 1, j) in space and (i, j) in space:
                count += 1
    return count


def solution():
    generation()
    N = int(input())
    for _ in range(N):
        x, y, d, g = map(int, input().split())
        move_rotate(x, y, d, g)
    result = count_square()
    print(result)


solution()
