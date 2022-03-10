import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # n: 회사 개수, m: 경로 개수
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split()) # 1번노드를 시작으로 k노드를 거쳐 x노드까지 가는 최소거리 구하기

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][k]+graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)