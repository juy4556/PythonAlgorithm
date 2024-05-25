# 2차원 리스트를 90도 회전한 결과를 반환하는 함수
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이
    m = len(a[0]) # 열 길이
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]  # 반시계는 result[m-j-1][i] = a[i][j]
    return result


def rotate_90_degree(space):
    n = len(space)
    m = len(space[0])
    arr = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            arr[j][n-1-i] = space[i][j]
    return arr


def rotate_180_degree(space):
    n = len(space)
    m = len(space[0])
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[n-i-1][m-j-1] = space[i][j]
    return arr


def rotate_270_degree(space):
    n = len(space)
    m = len(space[0])
    arr = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            arr[m-1-j][i] = space[i][j]
    return arr


space = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(space)
#시계방향
print("시계방향 90도:", rotate_90_degree(space))
print("시계방향 180도:", rotate_180_degree(space))
print("시계방향 270도:", rotate_270_degree(space))
