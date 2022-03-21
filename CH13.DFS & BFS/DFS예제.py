'''
INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph1 = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph1)

# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph2 = [[] for _ in range(3)]

graph2[0].append((1,7))
graph2[0].append((2,5))

graph2[1].append((0,7))

graph2[2].append((0,5))

print(graph2)
'''

# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [], # 노드 0에 연결된 정점 X
    [2, 3, 8], #노드 1에 연결된 정점: 2,3,8
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
