N = int(input())
arr = []
visited = [0] * 4
result = 0


def count_win(array, arr):
    count = 0
    for i in range(len(arr)):
        if (array[arr[i][0] - 1]) % 3 == array[arr[i][1] - 1] - 1:
            count += 1
    return count


def dfs(array, arr):
    global result, visited
    if len(array) >= 3:
        result = max(result, count_win(array, arr))
        return

    for i in range(1, 4):
        if not visited[i]:
            array.append(i)
            visited[i] = 1
            dfs(array, arr)
            array.pop()
            visited[i] = 0


for _ in range(N):
    arr.append(list(map(int, input().split())))

dfs([], arr)
print(result)
