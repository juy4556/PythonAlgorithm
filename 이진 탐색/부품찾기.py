''' 이진탐색으로 풀기
import sys
n = int(input()) # 부품 수
part = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input()) # 손님이 문의한 부품 번호 수
inquire = list(map(int, sys.stdin.readline().rstrip().split()))
arr = []
part.sort()
inquire.sort()

def binsearch(start, end, array, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    return None
for i in range(m):
    if binsearch(0,n-1,part,inquire[i]) == None:
        print("no",end=" ")
    else:
        print("yes",end=" ")
'''

''' 계수정렬을 활용한 풀이
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
inquire = list(map(int, input().split()))

for i in inquire:
    if array[i] == 1:
        print("yes",end=" ")
    else:
        print("no",end=" ")
'''
# set함수를 이용한 풀이
n = int(input())
array = set(map(int, input().split()))
m = int(input())
inquire = list(map(int, input().split()))

for i in inquire:
    if i in array:
        print("yes", end=" ")
    else:
        print("no", end=" ")