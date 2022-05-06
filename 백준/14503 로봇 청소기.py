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
        d = (d+3) % 4
        count += 1
        x = r + dx[d]
        y = c + dy[d]
        if 0 <= x <= N and 0 <= y <= M and space[x][y] == 0:
            r, c = x, y
            space[x][y] = 1
            result += 1
            return True
        if count == 4:
            if space[r - dx[d]][c - dy[d]] == 1:
                return False
            else:
                r, c = (r - dx[d]), (c - dy[d])
                return True



def solution():
    global result
    for _ in range(N):
        space.append(list(map(int, input().split())))

    space[r][c] = 1  # 첫 위치 청소
    result = 1
    while True:
        if not turn_left():
            break
        print(r, c, d)
    return result


print(solution())
