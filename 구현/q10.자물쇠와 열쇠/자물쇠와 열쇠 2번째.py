def rotate_a_matrix_by_90_degree(array):
    n = len(array) # 행 길이
    m = len(array[0]) # 열 길이
    new_arr = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_arr[j][m-1-i] = array[i][j]
    return new_arr

def check(array):
    length = len(array)//3
    for i in range(length, 2*length):
        for j in range(length, 2*length):
            if array[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)

        # x, y 좌표 기준으로 (2*n-1)씩 이동가능
        for x in range(2*n):
            for y in range(2*n):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock) == True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

