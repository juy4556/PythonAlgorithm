n, m = map(int, input().split())  # n은 세로길이, m은 가로길이(둘 다 1이상 1000이하)
count = 0  # 아이스크림 카운트 수
ice = []
for i in range(n):
    ice.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j):  # dfs(i,j)참일 때 카운트
            count += 1

print(count)
