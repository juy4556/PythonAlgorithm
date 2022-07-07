N = int(input())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))
result = 0


def left(arr):
    for i in range(N):  # 행
        j = 0
        k = j + 1
        while j < N and k < N:
            if arr[i][k] == 0:
                k += 1
                continue
            if arr[i][j] != arr[i][k]:
                j += 1
                k = j
            elif arr[i][j] == arr[i][k]:
                arr[i][j] *= 2
                arr[i][k] = 0
                j = k + 1
                k = j
            k += 1
        temp = []
        for l in range(N):
            if arr[i][l] != 0:
                temp.append(arr[i][l])
        length = len(temp)
        for _ in range(N - length):
            temp.append(0)
        arr[i] = temp
    return arr


def right(arr):
    for i in range(N):  # 행
        j = N - 1
        k = j - 1
        while j >= 0 and k >= 0:
            if arr[i][k] == 0:
                k -= 1
                continue
            if arr[i][j] != arr[i][k]:
                j -= 1
                k = j
            elif arr[i][j] == arr[i][k]:
                print(j, k)
                arr[i][j] *= 2
                arr[i][k] = 0
                j = k - 1
                k = j
            k -= 1
        temp = []
        for l in range(N - 1, -1, -1):
            if arr[i][l] != 0:
                temp.append(arr[i][l])
        length = len(temp)
        for _ in range(N - length):
            temp.append(0)
        temp.reverse()
        # print(temp)
        arr[i] = temp
    return arr


def up(arr):
    for i in range(N):  # 열
        j = 0
        k = j + 1
        while j < N and k < N:
            if arr[k][i] == 0:
                k += 1
                continue
            if arr[j][i] != arr[k][i]:
                j += 1
                k = j
            elif arr[j][i] == arr[k][i]:
                arr[j][i] *= 2
                arr[k][i] = 0
                j = k + 1
                k = j
            k += 1
        temp = []
        for l in range(N):
            if arr[l][i] != 0:
                temp.append(arr[l][i])
        length = len(temp)
        for _ in range(N - length):
            temp.append(0)
        for l in range(N):
            arr[l][i] = temp[l]
    return arr


def down(arr):
    for i in range(N):  # 열
        j = N - 1
        k = j - 1
        while j >= 0 and k >= 0:
            if arr[k][i] == 0:
                k -= 1
                continue
            if arr[j][i] != arr[k][i]:
                j -= 1
                k = j
            elif arr[j][i] == arr[k][i]:
                arr[j][i] *= 2
                arr[k][i] = 0
                j = k - 1
                k = j
            k -= 1
        temp = []
        for l in range(N):
            if arr[l][i] != 0:
                temp.append(arr[l][i])
        length = len(temp)
        for _ in range(N - length):
            temp.append(0)
        temp.reverse()
        for l in range(N):
            arr[l][i] = temp[l]
    return arr


def dfs(array, M):
    global result
    # for l in range(N):
    #     for m in range(N):
    #         print(arr[l][m], end=' ')
    #     print()
    # print("===========================")
    if M == 5:
        max_num = 0
        for i in range(N):
            max_num = max(max_num, max(array[i]))
        result = max(result, max_num)
        return
    dfs(left(array), M + 1)
    dfs(right(array), M + 1)
    dfs(up(array), M + 1)
    dfs(down(array), M + 1)


def solution():
    dfs(space, 0)
    print(result)


solution()