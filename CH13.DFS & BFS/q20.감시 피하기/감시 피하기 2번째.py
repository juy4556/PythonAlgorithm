import sys
input = sys.stdin.readline

n = int(input())
space = []
for i in range(n):
    space.append(list(input().split()))


def check(space):
    for i in range(n):
        for j in range(n):
            if space[i][j] == 'T':
                for k in range(i - 1, -1, -1):
                    if space[k][j] == 'S':
                        return False
                    elif space[k][j] == 'O':
                        break
                if i < n - 1:
                    for k in range(i + 1, n):
                        if space[k][j] == 'S':
                            return False
                        elif space[k][j] == 'O':
                            break
                for k in range(j - 1, -1, -1):
                    if space[i][k] == 'S':
                        return False
                    elif space[i][k] == 'O':
                        break
                    if j < n - 1:
                        for k in range(j + 1, n):
                            if space[i][k] == 'S':
                                return False
                            elif space[i][k] == 'O':
                                break
    return True



def dfs(space, count):
    if count == 3:
        if check(space):
            return True
        return False

    for i in range(n):
        for j in range(n):
            if space[i][j] == 'X':
                space[i][j] = 'O'
                flag = dfs(space, count + 1)
                if flag:
                    return True
                space[i][j] = 'X'

if dfs(space, 0):
    print("YES")
else:
    print("NO")
