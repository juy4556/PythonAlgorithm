import sys
import copy

input = sys.stdin.readline
N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(list(map(int, input().rstrip())))
for _ in range(N):
    B.append(list(map(int, input().rstrip())))


def check(A, B):
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True


cnt = 0
for i in range(0, N - 2):
    for j in range(0, M - 2):
        if A[i][j] != B[i][j]:
            cnt += 1
            for a in range(i, i + 3):
                for b in range(j, j + 3):
                    A[a][b] = 1 - A[a][b]

if check(A, B):
    print(cnt)
else:
    print(-1)
