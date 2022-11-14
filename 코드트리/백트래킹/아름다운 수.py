result = 0


def check(arr):
    start = 0
    end = 0
    while start < len(arr) and end < len(arr):
        while end+1 < len(arr) and arr[start] == arr[end+1]:
            end += 1
        if (end-start+1) % arr[start] > 0:
            return 0
        start = end+1
        end += 1
    return 1


def dfs(arr, k):
    global result
    if len(arr) == k:
        result += check(arr)
        return

    for i in range(1, 5):
        arr.append(i)
        dfs(arr, k)
        arr.pop()

n = int(input())
dfs([], n)

print(result)
