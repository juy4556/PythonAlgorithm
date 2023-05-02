R, C, M = map(int, input().split())
space = [[[] for _ in range(C)] for _ in range(R)]
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())  # r,c 좌표, s는 속력, d는 이동 방향, z는 크기
    space[r - 1][c - 1].append([s, d, z])


def capture_shark(n):
    global space, result
    for r in range(R):
        if len(space[r][n]) > 0:
            result += space[r][n][0][2]
            space[r][n] = []
            break


def move_shark(r, c, a):
    speed, dir, size = a[0][0], a[0][1], a[0][2]
    if dir == 1 or dir == 2:
        temp = speed % (2 * R - 2)
        for t in range(temp):
            if r == 0:
                dir = 2
            elif r == R - 1:
                dir = 1
            if 0 <= r + dx[dir - 1] <= R - 1:
                r += dx[dir - 1]
    elif dir == 3 or dir == 4:
        temp = speed % (2 * C - 2)
        for t in range(temp):
            if c == 0:
                dir = 3
            elif c == C - 1:
                dir = 4
            if 0 <= c + dy[dir - 1] <= C - 1:
                c += dy[dir - 1]
    return r, c, speed, dir, size


def solution():
    global space
    for n in range(C):
        for r in range(R):
            for c in range(C):
                if len(space[r][c]) > 1:  # 같은 구역에 2마리 이상의 상어가 있을 때
                    space[r][c].sort(key=lambda a: (-a[2]))  # 사이즈 기준 오름차순
                    space[r][c] = space[r][c][:1]
        capture_shark(n)
        new_space = [[[] for _ in range(C)] for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if len(space[r][c]) > 0:
                    new_r, new_c, speed, dir, size = move_shark(r, c, space[r][c])
                    new_space[new_r][new_c].append([speed, dir, size])
        for r in range(R):
            for c in range(C):
                if len(new_space[r][c]) > 1:  # 같은 구역에 2마리 이상의 상어가 있을 때
                    new_space[r][c].sort(key=lambda a: (-a[2]))  # 사이즈 기준 오름차순
                    new_space[r][c] = new_space[r][c][:1]
        space = new_space
    print(result)


solution()
