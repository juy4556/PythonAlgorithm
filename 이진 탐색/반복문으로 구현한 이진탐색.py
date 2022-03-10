# 반복문으로 구현한 이진탐색
def binary_search(start, end, array, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

array.sort()
result = binary_search(0,n,array,target)
if result == None:
    print("해당 원소 X")
else:
    print(result+1)