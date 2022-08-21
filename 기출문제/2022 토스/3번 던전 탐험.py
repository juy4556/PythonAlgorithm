k = int(input())  # 현재 체력
dungeons = [[80,20],[50,40],[30,10]]  # 요구체력, 사용체력 쌍
visited = [0] * (len(dungeons))
result = 0
def dfs(k, arr, temp):
    global result
    result = max(result, len(temp))
    print(temp)
    for i in range(len(arr)):
        require, use = arr[i][0], arr[i][1]
        if not visited[i] and k >= require:
            k -= use
            visited[i] = 1
            temp.append(i)
            dfs(k, arr, temp)
            k += use
            temp.pop()
            visited[i] = 0


dfs(k, dungeons,[])
print(result)