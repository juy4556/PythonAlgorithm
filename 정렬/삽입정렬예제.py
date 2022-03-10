array = [3, 1, 2, 6, 7, 5, 4]

# 삽입정렬에서 첫번째 요소는 그 자체로 정렬되어 있다고 판단하기 때문에 1~len(array)까지
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)
