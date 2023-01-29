import sys

input = sys.stdin.readline
N = int(input())  # 도시 수
M = int(input())  # 여행 계획에 속한 도시들의 수
parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:  # 루트노드 아니면
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            union_parent(parent, i + 1, j + 1)

plan = list(map(int, input().split()))
root = find_parent(parent, plan[0])
flag = 0
for i in range(1, len(plan)):
    if root != find_parent(parent, plan[i]):
        flag = 1
        break
if flag:
    print("NO")
else:
    print("YES")
