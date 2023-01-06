import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
parent = list(map(int, input().split()))  # 0 ~ N-1번 노드의 부모 정보
delete = int(input())
root = 0
node = deque()  # 지울 노드
for i in range(len(parent)):
    if parent[i] == -1:
        root = i
node.append(delete)


def find_leaf(tree):
    cnt = 0
    for t in range(len(tree) - 1, -1, -1):
        if t in tree or tree[t] == -2:
            continue
        else:
            cnt += 1
    return cnt


while node:
    now = node.popleft()
    for i in range(len(parent) - 1, -1, -1):
        if parent[i] == now:
            node.append(i)
            parent[i] = - 2  # 삭제 처리
parent[delete] = -2  # 삭제 처리
print(find_leaf(parent))
