array = [5, 3, 8, 1, 6, 2, 9, 0, 4, 7]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개일 때
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1
        if left >= right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)  # 피벗보다 작은 파티션 정렬
    quick_sort(array, right + 1, end)  # 피벗보다 큰 파티션 정렬


quick_sort(array, 0, len(array) - 1)
print(array)