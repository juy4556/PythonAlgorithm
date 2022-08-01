# 2차원 리스트를 90도 회전한 결과를 반환하는 함수
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이
    m = len(a[0]) # 열 길이
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]  # 반시계는 result[m-j-1][i] = a[i][j]
    return result

space = [[1,2,3,4] for _ in range(4)]
print(space)
#시계방향
space = list(map(list, zip(*space[::-1])))
print(space)
#반시계방향
space = [[1,2,3,4] for _ in range(4)]
space = list(map(list, zip(*space)))[::-1]
print(space)