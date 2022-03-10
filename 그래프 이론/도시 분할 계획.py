import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
edges=[]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b)) # c(cost)를 기준으로 정렬위함

edges.sort()
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

result = 0
cost = 0
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        result += c
        union_parent(parent, a, b)
        cost = c

result -= cost # 스패닝 트리를 2개로 만들기 위해 마지막 추가한 간선의 비용 차감
print(result)