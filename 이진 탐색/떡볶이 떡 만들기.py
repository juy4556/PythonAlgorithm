import sys

n, m = map(int, input().split())
height = list(map(int, sys.stdin.readline().rstrip().split()))

# 여기서 target은 m
def binsearch(start, end, minlength, array):
    mid_min = 0
    while start <= end:
        sum = 0
        mid = (start + end) // 2

        for i in range(n):
            if (array[i] - mid) > 0:
                sum += (array[i] - mid)

        if sum < minlength:
            end = mid - 1
        else:
            start = mid + 1
            mid_min = mid
    return mid_min


print(binsearch(0, max(height), m, height))
