import copy

N = int(input())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))
result = 0


def move(arr, d):
    if d == 0:  # 동
        for i in range(N):  # 행
            std = N - 1
            for j in range(N - 2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    if arr[i][std] == tmp:
                        arr[i][std] *= 2
                        std -= 1
                        arr[i][j] = 0

                    elif arr[i][std] == 0:
                        arr[i][std] = tmp
                        arr[i][j] = 0

                    else:
                        std -= 1
                        arr[i][std] = tmp
                        if std != j:
                            arr[i][j] = 0

    elif d == 1:  # 남
        for i in range(N):  # 행
            std = N - 1
            for j in range(N - 2, -1, -1):  # 열
                if arr[j][i]:
                    tmp = arr[j][i]
                    if arr[std][i] == tmp:
                        arr[std][i] *= 2
                        std -= 1
                        arr[j][i] = 0
                    elif arr[std][i] == 0:
                        arr[std][i] = tmp
                        arr[j][i] = 0

                    else:
                        std -= 1
                        arr[std][i] = tmp
                        if std != j:
                            arr[j][i] = 0

    elif d == 2:  # 서
        for i in range(N):  # 행
            std = 0
            for j in range(1, N):
                if arr[i][j]:
                    tmp = arr[i][j]
                    if arr[i][std] == tmp:
                        arr[i][std] *= 2
                        std += 1
                        arr[i][j] = 0
                    elif arr[i][std] == 0:
                        arr[i][std] = tmp
                        arr[i][j] = 0
                    else:
                        std += 1
                        arr[i][std] = tmp
                        if std != j:
                            arr[i][j] = 0

    elif d == 3:  # 북
        for i in range(N):  # 행
            std = 0
            for j in range(1, N):  # 열
                if arr[j][i]:
                    tmp = arr[j][i]
                    if arr[std][i] == tmp:
                        arr[std][i] *= 2
                        std += 1
                        arr[j][i] = 0

                    elif arr[std][i] == 0:
                        arr[std][i] = tmp
                        arr[j][i] = 0

                    else:
                        std += 1
                        arr[std][i] = tmp
                        if std != j:
                            arr[j][i] = 0
    return arr


def dfs(array, M):
    global result
    if M == 5:
        for i in range(N):
            result = max(result, max(array[i]))
        return

    # arr = [item[:] for item in array]
    for i in range(4):
        temp = move(copy.deepcopy(array), i)
        dfs(temp, M + 1)


def solution():
    dfs(space, 0)
    print(result)


solution()
