N, K = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))  # 0은 흰색, 1은 빨간색, 2는 파란색

graph = [[[] for _ in range(N)] for _ in range(N)]
horses = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for k in range(K):
    x, y, d = map(int, input().split())
    horses.append([x - 1, y - 1, d - 1])
    graph[x - 1][y - 1].append([k + 1, d - 1])  # K번 말 좌표 x,y 위치에 이동 방향은 d


def check():
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) >= 4:
                return True
    return False


def solution():
    turn = 0
    flag = False
    while True:
        turn += 1
        for k in range(len(horses)):
            temp = []
            x, y, d = horses[k][0], horses[k][1], horses[k][2]
            new_x, new_y = x + dx[d], y + dy[d]
            if new_x < 0 or new_x > N - 1 or new_y < 0 or new_y > N - 1 or space[new_x][new_y] == 2:  # 체스판 벗어나거나 파란색
                if d % 2 == 0:
                    d += 1
                elif d % 2 == 1:
                    d -= 1
                new_x, new_y = x + dx[d], y + dy[d]
                horses[k][2] = d
                if new_x < 0 or new_x > N - 1 or new_y < 0 or new_y > N - 1 or space[new_x][new_y] == 2:
                    pass  # 또 다시 체스판을 벗어나거나 파란색일 경우 이동 방향만 바꿔주고 위치는 변경 X
                else:
                    horses[k][0], horses[k][1] = new_x, new_y
                    if space[new_x][new_y] == 0:
                        for i in range(len(graph[x][y])):
                            if graph[x][y][i][0] == k + 1:
                                for j in range(i, len(graph[x][y])):
                                    horses[graph[x][y][j][0] - 1][0], horses[graph[x][y][j][0] - 1][1] = new_x, new_y
                                temp = graph[x][y][i:]
                                graph[x][y] = graph[x][y][:i]
                                break
                        graph[new_x][new_y] += temp
                    elif space[new_x][new_y] == 1:  # 빨간색
                        for i in range(len(graph[x][y])):
                            if graph[x][y][i][0] == k + 1:
                                for j in range(i, len(graph[x][y])):
                                    horses[graph[x][y][j][0] - 1][0], horses[graph[x][y][j][0] - 1][1] = new_x, new_y
                                temp = graph[x][y][i:]
                                temp.reverse()
                                graph[x][y] = graph[x][y][:i]
                                break
                        graph[new_x][new_y] += temp

            elif space[new_x][new_y] == 0:  # 흰색
                for i in range(len(graph[x][y])):
                    if graph[x][y][i][0] == k + 1:
                        for j in range(i, len(graph[x][y])):
                            horses[graph[x][y][j][0] - 1][0], horses[graph[x][y][j][0] - 1][1] = new_x, new_y
                        temp = graph[x][y][i:]
                        graph[x][y] = graph[x][y][:i]
                        break
                graph[new_x][new_y] += temp
            elif space[new_x][new_y] == 1:  # 빨간색
                for i in range(len(graph[x][y])):
                    if graph[x][y][i][0] == k + 1:
                        for j in range(i, len(graph[x][y])):
                            horses[graph[x][y][j][0] - 1][0], horses[graph[x][y][j][0] - 1][1] = new_x, new_y
                        temp = graph[x][y][i:]
                        temp.reverse()
                        graph[x][y] = graph[x][y][:i]
                        break
                graph[new_x][new_y] += temp
            if check() or turn > 1000:
                flag = True
                break
        if flag:
            break

    if turn > 1000:
        print(-1)
    else:
        print(turn)


solution()
