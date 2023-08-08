def dfs(arr, num, n, m):
    global result
    if len(arr) == m:
        print(*arr)
        return
    for i in range(N):
        if not visited[i]:
            arr.append(num[i])
            visited[i] = 1
            dfs(arr, num, n, m)
            visited[i] = 0
            arr.pop()


if __name__ == "__main__":
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()
    visited = [0 for _ in range(N)]
    result = []
    dfs([], num, N, M)
