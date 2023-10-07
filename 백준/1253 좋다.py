# 투 포인터
# N = int(input())
# A = list(map(int, input().split()))
# A.sort()
# i, j = 0, N - 1
# result = 0
# index = 0
#
# for index in range(N):
#     target = A[index]
#     i, j = 0, N - 1
#     if i == index:
#         i += 1
#     if j == index:
#         j -= 1
#     while i < N and j >= 0:
#         if i >= j:
#             break
#         if A[i] + A[j] == A[index]:
#             result += 1
#             break
#         elif A[i] + A[j] < A[index]:
#             i += 1
#             if i == index:
#                 i += 1
#         elif A[i] + A[j] > A[index]:
#             j -= 1
#             if j == index:
#                 j -= 1
#
# print(result)


N = int(input())
A = list(map(int, input().split()))
A.sort()
result = 0

for i in range(N):
    target = A[i]
    start, end = 0, N - 1
    flag = 0

    for s in range(N - 1):
        if flag:
            break
        if s == i:
            continue
        start = s + 1
        if start == i:
            start += 1
        if end == i:
            end -= 1

        while start <= end:
            mid = (start + end) // 2
            if A[s] + A[mid] == target:
                if mid != i:
                    flag = 1
                break
            elif A[s] + A[mid] > target:
                end = mid - 1
                if end == i:
                    end -= 1
            else:
                start = mid + 1
                if start == i:
                    start += 1
    if flag:
        result += 1

print(result)
