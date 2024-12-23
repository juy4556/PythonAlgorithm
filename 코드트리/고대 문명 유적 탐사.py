from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
peices_q = []


def rotate90(space, sx, sy, length):
    new_space = copy_space(space)
    acq = 0

    for i in range(sx, sx + length):
        for j in range(sy, sy + length):
            ox, oy = i - sx, j - sy
            rx, ry = oy, length - ox - 1
            new_space[sx + rx][sy + ry] = space[i][j]

    new_space, visited, delete_set, cnt = has_found(new_space)

    acq += cnt

    return new_space, acq, visited, delete_set


def rotate180(space, sx, sy, length):
    new_space = copy_space(space)
    acq = 0

    for i in range(sx, sx + length):
        for j in range(sy, sy + length):
            ox, oy = i - sx, j - sy
            rx, ry = length - ox - 1, length - oy - 1
            new_space[sx + rx][sy + ry] = space[i][j]

    new_space, visited, delete_set, cnt = has_found(new_space)

    acq += cnt

    return new_space, acq, visited, delete_set


def rotate270(space, sx, sy, length):
    new_space = copy_space(space)
    acq = 0

    for i in range(sx, sx + length):
        for j in range(sy, sy + length):
            ox, oy = i - sx, j - sy
            rx, ry = length - oy - 1, ox
            new_space[sx + rx][sy + ry] = space[i][j]

    new_space, visited, delete_set, cnt = has_found(new_space)

    acq += cnt

    return new_space, acq, visited, delete_set


def fill_space(space):
    global peices_q

    for j in range(5):
        for i in range(4, -1, -1):
            if space[i][j] == 0 and peices_q:
                space[i][j] = peices_q.popleft()

    # print("after fill")
    # for i in range(5):
    #     for j in range(5):
    #         print(space[i][j], end=' ')
    #     print()
    # print("========")
    return space


def has_found(space):
    visited = [[0 for _ in range(len(space[0]))] for _ in range(len(space))]
    count = 0
    delete_set = set()
    idx = 1

    for i in range(len(space)):
        for j in range(len(space[0])):
            if visited[i][j] == 0:
                visited, cnt = bfs(space, visited, i, j, idx)

                if cnt >= 3:
                    count += cnt
                    delete_set.add(idx)

                idx += 1

    return space, visited, delete_set, count


def acquire_items(space, delete_set, visited):
    # print("after delete")
    for i in range(len(space)):
        for j in range(len(space[0])):
            if visited[i][j] in delete_set:
                space[i][j] = 0
    #         print(space[i][j], end=' ')
    #     print()
    # print("========")

    space = fill_space(space)

    return space


def copy_space(space):
    new_space = [[0 for _ in range(5)] for _ in range(5)]

    for i in range(5):
        for j in range(5):
            new_space[i][j] = space[i][j]

    return new_space


def bfs(space, visited, a, b, idx):
    count = 0
    num = space[a][b]
    q = deque()
    q.append((a, b))
    visited[a][b] = idx

    while (q):
        x, y = q.popleft()
        count += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if is_not_in_range(nx, ny, len(space), len(space[0])):
                continue
            if visited[nx][ny] or space[nx][ny] != num:
                continue

            visited[nx][ny] = idx
            q.append((nx, ny))

    return visited, count


def is_not_in_range(x, y, row_length, col_length):
    return x < 0 or x >= row_length or y < 0 or y >= col_length


if __name__ == "__main__":
    K, M = map(int, input().split())
    space = [[0 for _ in range(5)] for _ in range(5)]
    turn = 0

    for i in range(5):
        space[i] = list(map(int, input().split()))

    pieces = list(map(int, input().split()))
    peices_q = deque(pieces)

    while turn < K:
        rotate_degree = 360
        acquire = -1
        new_space = []
        visited = []
        delete_set = set()
        rx, ry = 2, 2
        for j in range(2, -1, -1):
            for i in range(2, -1, -1):
                space1, a, visited1, delete_set1 = rotate90(space, i, j, 3)
                space2, b, visited2, delete_set2 = rotate180(space, i, j, 3)
                space3, c, visited3, delete_set3 = rotate270(space, i, j, 3)

                ns, acq, degree = [], 0, 400
                temp_visited = []
                temp_delete = set()

                if a >= b:
                    if a >= c:
                        acq = a
                        ns = space1
                        temp_visited = visited1
                        temp_delete = delete_set1
                        degree = 90
                    else:
                        acq = c
                        ns = space3
                        temp_visited = visited3
                        temp_delete = delete_set3
                        degree = 270
                else:
                    if b >= c:
                        acq = b
                        ns = space2
                        temp_visited = visited2
                        temp_delete = delete_set2
                        degree = 180
                    else:
                        acq = c
                        ns = space3
                        temp_visited = visited3
                        temp_delete = delete_set3
                        degree = 270

                if acquire > acq:
                    continue

                if acquire < acq:
                    new_space = ns
                    acquire = acq
                    rotate_degree = degree
                    visited = temp_visited
                    delete_set = temp_delete
                    rx, ry = i, j
                elif acquire == acq:
                    if rotate_degree >= degree:
                        new_space = ns
                        acquire = acq
                        rotate_degree = degree
                        visited = temp_visited
                        delete_set = temp_delete
                        rx, ry = i, j

        # print("돌린 왼쪽 위:", rx, ry, "돌린 각도: ", rotate_degree)
        # for i in range(5):
        #     for j in range(5):
        #         print(new_space[i][j], end=' ')
        #     print()
        # print("========")
        new_space = acquire_items(new_space, delete_set, visited)

        while True:
            new_space, visited, delete_set, count = has_found(new_space)
            if count == 0:
                break
            acquire += count
            new_space = acquire_items(new_space, delete_set, visited)

        space = new_space
        # for i in range(5):
        #     for j in range(5):
        #         print(space[i][j], end=' ')
        #     print()
        # print("========")
        if acquire == 0:
            break
        print(acquire, end=' ')
        turn += 1
