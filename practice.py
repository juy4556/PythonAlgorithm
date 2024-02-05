'''
'숫자고르기'
'''
# 24.01.30 15:12 ~
import sys

input = sys.stdin.readline


def dfs(index):
    if visit[index] == 2 or answer[array[index] - 1] == 1:
        return
    else:
        visit[index] += 1
        if visit[index] == 2:
            answer[array[index] - 1] = 1
        dfs(array[index] - 1)


N = int(input())
array = []
for i in range(N):
    array.append(int(input()))
answer = [0 for _ in range(N)]

for i in range(N):
    value = array[i] - 1
    if answer[value] == 0:
        visit = [0 for _ in range(N)]
        dfs(i)

length = 0
for i in range(N):
    if answer[i] == 1:
        length += 1

print(length)
for i in range(N):
    if answer[i] == 1:
        print(i + 1)
