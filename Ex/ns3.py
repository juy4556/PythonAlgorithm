paper = [1, 2, 4, 8, 16]
ans = -1


def dfs(arr, count, n):
    global ans
    if count > n:
        return
    else:
        ans = max(ans, max(arr))
        for i in range(len(arr) - 1):
            temp = arr[i + 1:]
            temp1 = arr[i::-1]
            print("temp, temp1", temp, temp1)
            for j in range(len(temp1)):
                if len(temp) > j:
                    temp[j] += temp1[j]
                else:
                    temp.append(temp1[j])
            print(temp, count+1)
            dfs(temp, count + 1, n)


dfs(paper, 0, 3)
print(ans)
