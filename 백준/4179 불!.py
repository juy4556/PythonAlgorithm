import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def move(person, visited):
    new_person = []
    for x, y in person:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx > R - 1 or ny > C - 1 or space[nx][ny] == '#':
                continue
            if not visited[nx][ny] and space[nx][ny] == '.':
                space[nx][ny] = 'J'
                visited[nx][ny] = 1
                new_person.append([nx, ny])
    return new_person


def spread_fire(fire, visited):
    new_fire = []
    for x, y in fire:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx > R - 1 or ny > C - 1 or space[nx][ny] == '#':
                continue
            if not visited[nx][ny]:
                if space[nx][ny] == 'J' and [nx, ny] in person:
                    person.remove([nx, ny])
                space[nx][ny] = 'F'
                visited[nx][ny] = 1
                new_fire.append([nx, ny])
    return new_fire


def check(person):
    if len(person) == 0:
        return 0

    for x, y in person:
        if x == 0 or x == R - 1 or y == 0 or y == C - 1 and space[x][y] != 'F':
            return 2

    return 1


if __name__ == "__main__":
    R, C = map(int, input().split())
    time = 1
    space = []
    person = []
    fire = []
    person_visited = [[0 for _ in range(C)] for _ in range(R)]
    fire_visited = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        col = list(' '.join(input().rstrip()).split())
        space.append(col)
        for c in range(len(col)):
            if space[r][c] == 'J':
                person.append([r, c])
                person_visited[r][c] = 1
            elif space[r][c] == 'F':
                fire.append([r, c])
                fire_visited[r][c] = 1

    if check(person) == 2:
        print(time)
        exit()
    flag = 0
    while True:
        time += 1
        person = move(person, person_visited)
        fire = spread_fire(fire, fire_visited)
        flag = check(person)

        if flag == 0 or flag == 2:
            break

    if flag == 0:
        print("IMPOSSIBLE")
    elif flag == 2:
        print(time)
