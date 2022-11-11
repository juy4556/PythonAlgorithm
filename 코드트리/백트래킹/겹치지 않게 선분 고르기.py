def check(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i][1] >= arr[i+1][0]:
            return 1
    return 0


def dfs(arr, lines, k):
    global result
    if check(arr):
        return
    result = max(result, len(arr))
    for i in range(k, n):
        arr.append(lines[i])
        dfs(arr, lines, i+1)
        arr.pop()


if __name__ == "__main__":
    result = -1
    n = int(input())
    lines = []
    for _ in range(n):
        x1, x2 = map(int, input().split())
        lines.append((x1, x2))

    lines.sort(key = lambda x: x[0])
    dfs([], lines, 0)
    print(result)
