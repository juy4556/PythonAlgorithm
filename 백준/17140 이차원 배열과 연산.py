r, c, k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))


def operation(A):
    temp = []
    length = 0
    for i in range(len(A)):
        kinds = set(A[i])
        tmp = []
        for kind in kinds:
            if kind == 0:
                continue
            tmp.append((kind, A[i].count(kind)))
        length = max(length, len(kinds) * 2)
        temp.append(tmp)
        temp[i].sort(key=lambda x: (x[1], x[0]))

    tmp = [[0] * length for _ in range(len(A))]
    for i in range(len(temp)):
        idx = 0
        for j in range(len(temp[i])):
            tmp[i][idx] = temp[i][j][0]
            tmp[i][idx + 1] = temp[i][j][1]
            idx += 2
    return tmp


def check(A, r, c, k):
    if r - 1 < len(A) and c - 1 < len(A[0]):
        if A[r - 1][c - 1] == k:
            return True
    return False


def solution(A, r, c, k):
    time = 0

    while time < 101:
        if check(A, r, c, k):
            print(time)
            break
        time += 1
        if len(A) >= len(A[0]):
            A = operation(A)
        else:
            A = list(map(list, zip(*A)))
            A = operation(A)
            A = list(map(list, zip(*A)))
        if time >= 101:
            print(-1)


solution(A, r, c, k)