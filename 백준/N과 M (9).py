def dfs(arr, n, m):
    global result
    if len(arr) == m:
        result.append(arr[:])
        return
    for i in range(N):
        if not visited[i]:
            arr.append(num[i])
            visited[i] = 1
            dfs(arr, n, m)
            visited[i] = 0
            arr.pop()


if __name__ == "__main__":
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()
    visited = [0 for _ in range(N)]
    result = []
    dfs([], N, M)
    result.sort()
    print(*result[0])
    for i in range(1, len(result)):
        if result[i] == result[i - 1]:
            continue
        print(*result[i])
