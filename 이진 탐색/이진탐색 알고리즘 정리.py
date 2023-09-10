from bisect import bisect_left, bisect_right


def bin_search1(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid - 1
            continue
        start = mid + 1
    return start, end, mid


def bin_search2(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid - 1
            continue
        start = mid + 1
    return start, end, mid


a = [1, 63, 46, 36, 246, 43, 57, 63, 34, 6578, 467, 534, 23, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 11, 11, 1, 1, 2]
a.sort()
print(a)
print(bisect_left(a, 1), bisect_right(a, 1))
print(bin_search1(a, 1))
print(bin_search2(a, 1))
