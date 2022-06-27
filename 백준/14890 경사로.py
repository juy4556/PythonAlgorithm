N, L = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))

result = 0


def find_column(i):
    global result
    visited = [0] * N # 경사로 둔 위치
    col = space[0][i]
    col_flag = True
    j = 1
    while j < N:
        flag1 = True
        if abs(col - space[j][i]) == 0:
            pass
        elif abs(col - space[j][i]) == 1:
            if col > space[j][i]:  # 뒤쪽이 더 작을 때
                if j + L <= N and not visited[j]:
                    for k in range(j + 1, j + L):
                        if space[j][i] != space[k][i] or visited[k]:  # j부터 j+L-1까지 칸의 높이가 같은지와 L개의 칸이 연속되어 있는지 확인
                            flag1 = False
                            col_flag = False
                            break
                    if flag1:
                        for k in range(j, j + L):
                            visited[k] = 1
                        col = space[j + L - 1][i]
                        j += L - 1
                    else:
                        break
                else:
                    col_flag = False
                    break
            else:  # 앞쪽이 더 작을 때
                if j - L >= 0 and not visited[j]:
                    for k in range(j - L, j):
                        if space[j-1][i] != space[k][i] or visited[k]:
                            flag1 = False
                            col_flag = False
                            break
                    if flag1:
                        for k in range(j-L, j):
                            visited[k] = 1
                        col = space[j][i]
                else:
                    col_flag = False
                    break
        else:
            col_flag = False
            break
        j += 1
    if col_flag:
        result += 1


def find_row(i):
    global result
    row = space[i][0]
    row_flag = True
    visited = [0] * N  # 경사로 둔 위치
    j = 1
    while j < N:
        flag1 = True
        if abs(row - space[i][j]) == 0:
            pass
        elif abs(row - space[i][j]) == 1:
            if row > space[i][j]:  # 뒤쪽이 더 작을 때
                if j + L <= N and not visited[j]:
                    for k in range(j + 1, j + L):
                        if space[i][j] != space[i][k] or visited[k]:  # j부터 j+L-1까지 칸의 높이가 같은지와 L개의 칸이 연속되어 있는지 확인
                            flag1 = False
                            row_flag = False
                            break
                    if flag1:
                        for k in range(j, j + L):
                            visited[k] = 1
                        row = space[i][j + L - 1]
                        j += L - 1
                    else:
                        break
                else:
                    row_flag = False
                    break
            else:  # 앞쪽이 더 작을 때
                if j - L >= 0 and not visited[j]:
                    for k in range(j - L, j):
                        if space[i][j-1] != space[i][k] or visited[k]:
                            flag1 = False
                            row_flag = False
                            break
                    if flag1:
                        for k in range(j - L, j):
                            visited[k] = 1
                        row = space[i][j]
                else:
                    row_flag = False
                    break
        else:
            row_flag = False
            break
        j += 1
    if row_flag:
        result += 1


def solution():
    for i in range(N):
        find_column(i)
        find_row(i)

    print(result)


solution()
