'''
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1
'''
# 재귀함수로 구현한 이진탐색
'''
def binary_search(start,end,array,target):
    if start>end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(start,mid-1,array,target)
    else:
        return binary_search(mid+1, end, array, target)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

array.sort()
result = binary_search(0,n-1,array,target)
if result == None:
    print("원소 존재 X")
else:
    print(result+1)
'''

