v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = False
def dfs(i):
    global result
    visited[i] = True
    for node in graph[i]:
        print(node, end=' ')
        print(visited[node])
        if visited[node] == False:
            dfs(node)
        else:
            result = True
            return True
    return False
dfs(1)
print(result)
if result:
    print("사이클 발생")
else:
    print("사이클 발생하지 않음")