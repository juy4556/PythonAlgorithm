import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
count = 0
array = []

for i in range(n):
    array.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if array[x][y] == 0:
        array[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            dfs(i,j)
            count+=1

print(count)