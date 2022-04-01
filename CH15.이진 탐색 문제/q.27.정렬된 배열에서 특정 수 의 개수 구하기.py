import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num = list(map(int, input().split()))

start = 0
end = n-1
count = 0
while start < end:
    mid = (start + end) // 2
    if num[mid] == k:
        m = mid
        count = 1
        while num[m-1] == k:
            count += 1
            m -= 1
        while num[mid+1] == k:
            count += 1
            mid += 1
        break
    elif num[mid] < k:
        start = mid + 1
    elif num[mid] > k:
        end = start - 1

if count == 0:
    print(-1)
else:
    print(count)

