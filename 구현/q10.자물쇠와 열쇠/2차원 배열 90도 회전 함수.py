def rotate_a_matrix_by_90_degree(array):
    len(array) = n # 행 길이
    len(array[0]) = m # 열 길이
    new_arr = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_arr[j][m-1-i] = array[i][j]
    return new_arr
