import sys
input = sys.stdin.readline
x, y = map(int, input().split())
z = y*100 // x
start, end = 1, x
if z >= 99:
    print(-1)
else:
    result = 0
    while start <= end:
        mid = (start+end) // 2

        if (y+mid)*100//(x+mid) <= z:
            start = mid+1
        else:
            result = mid
            end = mid-1
    print(result)