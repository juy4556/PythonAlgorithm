# n, m = 4, 6
# arr = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
# temp = [[0] * m for _ in range(n)]
#
# # 1. 반복문
# for i in range(m):
#     for j in range(n):
#         temp[i][j] = arr[n - 1 - j][i]
# #
# # # 2. zip함수
# # arr = list(map(list, zip(*arr[::-1]))
# print(temp)
# arr = []
# R, C, T = map(int, input().split())
#
# for _ in range(R):
#     arr.append(list(map(int, input().split())))
# n = R  # 행 길이
# m = C  # 열 길이
# result = [[0] * n for _ in range(m)]  # 결과 리스트
# for i in range(n):
#     for j in range(m):
#         result[m-j-1][i] = arr[i][j]
#
# print(result)

arr= [1,2,3,4,5]
arr.insert(1, 0)
print(arr)