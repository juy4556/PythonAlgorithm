N, M = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))
score = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, -1, 0]
count, rainbow = 0, 0


def dfs(x, y, graph, num):
    global count, rainbow
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1 or graph[nx][ny] != 0 or space[nx][ny] < 0:
            continue
        if space[nx][ny] == num:
            graph[nx][ny] = num
        elif space[nx][ny] == 0:
            rainbow += 1
            graph[nx][ny] = num
            dfs(nx, ny, graph, num)
            count += 1


def remove_block(blocks):
    for i in range(N):
        for j in range(N):
            if blocks[i][j] > 0:
                space[i][j] = -2  # 빈 칸을 -2로 초기화


def gravity():
    for i in range(N):
        j = N - 1
        while j > 0:
            if space[j][i] == -1:
                j -= 1
                continue
            elif space[j][i] == -2:
                k = j - 1
                while k > -1:
                    if space[k][i] == -1:
                        j = k
                        break
                    elif space[k][i] >= 0:
                        # print(j, k, i)
                        space[k][i], space[j][i] = space[j][i], space[k][i]
                        break
                    k -= 1
            j -= 1


def rotate_counter_by_90degree(a):
    result = [[0 for _ in range(N)] for _ in range(N)]  # 결과 리스트
    for i in range(N):
        for j in range(N):
            result[N - j - 1][i] = a[i][j]
    return result


def solution():
    global count, rainbow, space, score
    blocks = [[0 for _ in range(N)] for _ in range(N)]
    block = [0, 0, 0]  # 무지개 블록 수, x, y
    while True:  # 일반 블록이 적어도 하나 있을 때까지 반복
        max_count = 0
        for i in range(N):
            for j in range(N):
                graph = [[0 for _ in range(N)] for _ in range(N)]
                count, rainbow = 0, 0
                if space[i][j] > 0:
                    dfs(i, j, graph, space[i][j])
                    if count > max_count:
                        max_count = count
                        block = [rainbow, i, j]
                        blocks = graph
                    elif count == max_count:
                        if rainbow >= block[0]:
                            block = [rainbow, i, j]
                            blocks = graph
        print(block)

        if max_count < 2:  # 블록 그룹 없을 때 break
            break
        remove_block(blocks)
        print(space)
        score += pow(max_count, 2)
        gravity()
        print(space)
        space = rotate_counter_by_90degree(space)
        print(space)
        gravity()
        print(space)
        print(score)
        print("========================================================")
    print(score)


solution()
