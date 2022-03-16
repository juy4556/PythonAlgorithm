import sys

input = sys.stdin.readline

n = int(input())  # n은 3이상 6이하
hallway = []
for i in range(n):
    hallway.append(list(
        input().split()))  # 해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않다면 X. 단 전체 선생님 수는 5이하, 학생수는 30이하, 빈칸수는 3이상

def check(array):
    for i in range(n):
        for j in range(n):
            if array[i][j] == 'T':
                if i < n-1:
                    for x in range(i + 1, n):
                        if array[x][j] == 'O':
                            break
                        elif array[x][j] == 'S':
                            return False
                for x in range(i-1,-1,-1):
                    if array[x][j] == 'O':
                        break
                    elif array[x][j] == 'S':
                        return False

                if j < n-1:
                    for y in range(j+1, n):
                        if array[i][y] == 'O':
                            break
                        elif array[i][y] == 'S':
                            return False
                for y in range(j-1,-1,-1):
                    if array[i][y] == 'O':
                        break
                    elif array[i][y] == 'S':
                        return False
    return True


def dfs(array, count):
    if count == 3:
        if check(array):
            return True
        return

    for i in range(n):
        for j in range(n):
            if array[i][j] == 'X':
                array[i][j] = 'O'
                if dfs(array, count+1):
                    return True
                array[i][j] = 'X'


if dfs(hallway, 0):
    print("YES")
else:
    print("NO")
