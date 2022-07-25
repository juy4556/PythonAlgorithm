N, M, k = map(int, input(), split())
space = []
smell = [[[0, 0] for _ in range(4)] for _ in range(4)]  # 상어번호와 상어 냄새 정보 기록
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    space.append(list(map(int, input().split())))
shark_dir = list(map(int, input().split()))  # 1~N번 상어의 진행 방향
shark_dir = [d-1 for d in shark_dir]
move_priority = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        move_priority[i].append(list(map(int, input().split())))


def shark_move():
    for i in range(N):
        for j in range(N):
            if space[i][j] == 0:
                continue
            shark_num = space[i][j]
            direction = shark_dir[shark_num-1]
            flag = False
            for l in range(4):
                d = move_priority[shark_num-1][direction][l]
                nx = i + dx[d]
                ny = j + dy[d]
                if not(0<=nx<N and 0<=ny<N) or smell[nx][ny][0] < shark_num:
                    continue
                if smell[nx][ny][1] == 0:  # 새 칸에 남아있는 냄새가 없을 때
                    flag = True
                    if space[nx][ny] == 0:
                        space[nx][ny] = space[i][j]
                        space[i][j] = 0
                    else:  # 새 칸에 다른 상어 있을 때
                if smell[nx][ny]smell[nx][ny][0] < shark_num:
                if smell[nx][ny][0] > 0:


def leave_smell():



def smell_light():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] == 0:
                continue
            elif smell[i][j][1] == 1:
                smell[i][j] = [0, 0]
            elif smell[i][j][1] > 1:
                smell[i][j][1] -= 1


def check_space():




def solution():
    for i in range(N):
        for j in range(N):
            if space[i][j] > 0:
                smell[i][j] = [space[i][j], 4]
    time = 0
    while True:
        time += 1
        if time>1000:
            time = -1
            break
        smell_light()
        shark_move()
        leave_smell()
        check_space()

    print(time)
