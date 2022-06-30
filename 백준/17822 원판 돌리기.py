N, M, T = map(int, input().split())
space = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(N):
    space.append(list(map(int, input().split())))


def rotate(x, d, k):
    for i in range(x - 1, N, x):
        for _ in range(k):
            if d:  # d가 1이면 반시계방향
                space[i] = space[i][1:M] + space[i][:1]
            else:  # d가 0이면 시계방향
                space[i] = space[i][M - 1:] + space[i][:M - 1]


def second_work():
    flag = False
    arr = []
    for _ in range(N):
        arr = [item[:] for item in space]
    for i in range(N):
        if space[i].count(0) != M:  # 원판에 수가 남아 있을 때
            for j in range(M):
                flag2 = False
                if 1 <= space[i][j] <= 1000:
                    for d in range(4):
                        nx = i + dx[d]
                        ny = (j + dy[d]) % M
                        if nx < 0 or nx > N - 1 or arr[nx][ny] == 0:
                            continue
                        if arr[nx][ny] == space[i][j]:
                            flag, flag2 = True, True
                            space[nx][ny] = 0
                if flag2:
                    space[i][j] = 0
    if not flag:
        temp = set()
        count, summary = 0, 0
        for i in range(N):
            for j in range(M):
                if space[i][j] > 0:
                    summary += space[i][j]
                    count += 1
                    temp.add((i, j))
        if count > 0:
            avg = summary / count
            for t1, t2 in temp:
                if space[t1][t2] > avg:
                    space[t1][t2] -= 1
                elif space[t1][t2] < avg:
                    space[t1][t2] += 1


def solution():
    for t in range(T):
        x, d, k = map(int, input().split())  # 번호가 x의 배수인 원판을 d방향으로 k칸 회전
        rotate(x, d, k)
        second_work()
    result = 0
    for i in range(N):
        result += sum(space[i])
    print(result)


solution()
