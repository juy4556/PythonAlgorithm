import copy

N, M, k = map(int, input().split())
space = []
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]  # 상어번호와 상어 냄새 정보 기록
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    space.append(list(map(int, input().split())))
shark_dir = list(map(int, input().split()))  # 1~N번 상어의 진행 방향
shark_dir = [d - 1 for d in shark_dir]
move_priority = [[] for _ in range(M)]
out = 0  # 벗어난 상어 수
for i in range(M):
    for j in range(M):
        s = list(map(int, input().split()))
        move_priority[i].append(s)


def shark_move():
    global out
    new_space = copy.deepcopy(space)
    for i in range(N):
        for j in range(N):
            if space[i][j] == 0:
                continue
            shark_num = new_space[i][j]
            direction = shark_dir[shark_num - 1]
            flag = False
            for l in range(4):
                d = move_priority[shark_num - 1][direction-1][l]
                nx = i + dx[d-1]
                ny = j + dy[d-1]
                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                if smell[nx][ny][1] == 0:  # 새 칸에 남아있는 냄새가 없을 때
                    flag = True
                    if new_space[nx][ny] == 0:  # 새 칸에 상어가 없을 때
                        new_space[nx][ny] = space[i][j]
                        new_space[i][j] = 0
                    else:  # 새 칸에 다른 상어 있을 때
                        if new_space[nx][ny] > new_space[i][j]:
                            new_space[nx][ny] = space[i][j]
                        out += 1
                        new_space[i][j] = 0
                    shark_dir[shark_num-1] = d
                    break
            if flag:
                continue
            for l in range(4):
                d = move_priority[shark_num - 1][direction-1][l]
                nx = i + dx[d-1]
                ny = j + dy[d-1]
                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                if smell[nx][ny][1] == shark_num:
                    space[nx][ny] = space[i][j]
                    space[i][j] = 0
                    shark_dir[shark_num-1] = d
                    break
    return new_space

def smell_light():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] == 0:
                continue
            elif smell[i][j][1] == 1:
                smell[i][j] = [0, 0]
            elif smell[i][j][1] > 1:
                smell[i][j][1] -= 1


def solution():
    global space

    time = 0
    while True:
        time += 1
        if time > 1000:
            time = -1
            break
        for i in range(N):
            for j in range(N):
                if space[i][j] > 0:
                    smell[i][j] = [k, space[i][j]]
        smell_light()
        space = shark_move()
        if out == M - 1:
            break

    print(time)


solution()
