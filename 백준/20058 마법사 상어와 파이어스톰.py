import copy
from collections import deque

N, Q = map(int, input().split())
A = []
for _ in range(pow(2, N)):
    A.append(list(map(int, input().split())))
L = list(map(int, input().split()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False for _ in range(pow(2, N))] for _ in range(pow(2, N))]


def rotate_90_degree(original):
    n = len(original)  # 행 길이
    m = len(original[0])  # 열 길이
    result = [[0] * n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = original[i][j]
    return result


def check(temp, r, c):
    count = 0
    for i in range(4):
        new_r = r + dx[i]
        new_c = c + dy[i]
        if new_r < 0 or new_c < 0 or new_r > pow(2, N) - 1 or new_c > pow(2, N) - 1:
            continue
        if A[new_r][new_c] > 0:
            count += 1
    if count < 3:
        if temp[r][c] > 0:
            temp[r][c] -= 1


def bfs(r, c):
    global visited
    count = 0
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        count += 1
        r, c = q.popleft()
        for i in range(4):
            new_r = r + dx[i]
            new_c = c + dy[i]
            if new_r < 0 or new_c < 0 or new_r > pow(2, N) - 1 or new_c > pow(2, N) - 1:
                continue
            if not visited[new_r][new_c] and A[new_r][new_c] > 0:
                q.append((new_r, new_c))
                visited[new_r][new_c] = True
    return count


def solution():
    global A, visited
    summary = 0
    count = 0

    for l in L:  # 파이어스톰 시전
        for i in range(0, pow(2, N), pow(2, l)):
            for j in range(0, pow(2, N), pow(2, l)):
                temp = [row[j:j + pow(2, l)] for row in A[i:i + pow(2, l)]]
                for p in range(pow(2, l)):
                    A[i:i + pow(2, l)][p][j:j + pow(2, l)] = rotate_90_degree(temp)[p]
        tempList = copy.deepcopy(A)
        for i in range(0, pow(2, N)):
            for j in range(0, pow(2, N)):
                check(tempList, i, j)
        A = tempList

    # 남아있는 얼음 A[r][c]합
    for i in range(0, pow(2, N)):
        for j in range(0, pow(2, N)):
            summary += A[i][j]
            if not visited[i][j] and A[i][j] > 0:
                count = max(count, bfs(i, j))

    print(summary)
    print(count)


solution()
