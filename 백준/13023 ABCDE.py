def dfs(now, visited):
    if visited[now] >= 5:
        return True
    for n in graph[now]:
        if not visited[n]:
            visited[n] = visited[now] + 1
            if dfs(n, visited):
                return True
            visited[n] = 0
    return False


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    result = 0
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(N):
        visited = [0 for _ in range(N)]
        visited[i] = 1
        if dfs(i, visited):
            result = 1
            break
    print(result)
