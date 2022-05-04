space = []
dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
result = 0


def turn_left():
    global r, c, d, result
    count = 0
    while True:
        d -= 1
        if d < 0:
            d = 3
        if count == 4:
            if space[r - dx[d]][c - dy[d]] == 1:
                return False
            else:
                r, c = (r - dx[d]), (c - dy[d])
                count = 0
        x = r-1 + dx[d]
        y = c-1 + dy[d]
        if space[x][y] == 0:
            r, c = x+1, y+1
            print(r, c, d)
            space[x][y] = 2  # 청소는 2
            result += 1
            return True
        count += 1


def solution():
    global result
    for _ in range(N):
        space.append(list(map(int, input().split())))

    space[r-1][c-1] = 2  # 첫 위치 청소
    result = 1
    while True:
        if not turn_left():
            break
        # for i in range(N):
        #     for j in range(M):
        #         print(space[i][j], end=' ')
        #     print()
    return result


print(solution())