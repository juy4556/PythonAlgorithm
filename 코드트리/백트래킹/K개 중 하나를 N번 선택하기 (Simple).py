def dfs(arr, k, n):
    if len(arr) == n:
        print(*arr)
        return
    for i in range(1, k+1):
        arr.append(i)
        dfs(arr, k, n)
        arr.pop()

K, N = map(int, input().split())
dfs([], K, N)
