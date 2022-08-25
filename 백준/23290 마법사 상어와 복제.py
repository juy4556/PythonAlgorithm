M, S = map(int, input().split())
space = [[[] for _ in range(4)] for _ in range(4)]
new_space = [[[] for _ in range(4)] for _ in range(4)]
fish_smell = [[0 for _ in range(4)] for _ in range(4)]
for _ in range(M):
    fx, fy, d = map(int, input().split())
    space[fx - 1][fy - 1].append(d - 1)

sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

shark_move_way = []


def dfs(array):
    if len(array) == 3:
        shark_move_way.append(list(array))
        return
    for i in range(1, 5):
        array.append(i)
        dfs(array)
        array.pop()


def init():
    dfs([])  # 상어 이동 방법 init


def reproduction():
    for i in range(4):
        for j in range(4):
            space[i][j] = new_space[i][j] + space[i][j]


def fish_move():
    global new_space
    new_space = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for d in space[i][j]:
                fx, fy = i, j
                flag = False
                for dir in range(8):
                    direction = (d - dir) % 8
                    nfx = fx + dx[direction]
                    nfy = fy + dy[direction]
                    if nfx < 0 or nfx > 3 or nfy < 0 or nfy > 3:
                        continue
                    if [nfx, nfy] == [sx, sy] or fish_smell[nfx][nfy] > 0:
                        continue
                    new_space[nfx][nfy].append(direction)
                    flag = True
                    break
                if not flag:
                    new_space[fx][fy].append(d)


def shark_move():
    global sx, sy
    sdx = [-1, 0, 1, 0]
    sdy = [0, -1, 0, 1]
    cnt = 0  # 잡아먹는 물고기 수
    route = []
    for a, b, c in shark_move_way:
        dir = [a - 1, b - 1, c - 1]
        visited = [[0 for _ in range(4)] for _ in range(4)]
        tsx, tsy = sx, sy
        temp_count = 0
        for i in range(3):
            nsx = tsx + sdx[dir[i]]
            nsy = tsy + sdy[dir[i]]
            if nsx < 0 or nsx > 3 or nsy < 0 or nsy > 3:
                continue
            tsx, tsy = nsx, nsy
            if not visited[nsx][nsy] and len(new_space[nsx][nsy]) > 0:
                visited[nsx][nsy] = 1
                temp_count += len(new_space[nsx][nsy])
        if cnt < temp_count:
            cnt = temp_count
            route = dir
    if (len(route)):
        for i in range(3):
            nsx = sx + sdx[route[i]]
            nsy = sy + sdy[route[i]]
            sx, sy = nsx, nsy
            if len(new_space[sx][sy]) > 0:
                new_space[sx][sy] = []
                fish_smell[sx][sy] = 3  # 물고기 냄새 남김

def lose_fish_smell():
    for i in range(4):
        for j in range(4):
            if fish_smell[i][j] > 0:
                fish_smell[i][j] -= 1


def check():
    for i in range(4):
        for j in range(4):
            print(space[i][j], end=" ")
        print()
    print("==============================")


def new_check():
    for i in range(4):
        for j in range(4):
            print(new_space[i][j], end=" ")
        print()
    print("-----------------------------------")


def solution():
    init()
    for _ in range(S):
        fish_move()
        # print("FISHMOVEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        # new_check()
        shark_move()
        lose_fish_smell()
        # check()
        # new_check()
        reproduction()
        # check()

    result = 0
    for i in range(4):
        for j in range(4):
            result += len(space[i][j])
    print(result)


solution()
