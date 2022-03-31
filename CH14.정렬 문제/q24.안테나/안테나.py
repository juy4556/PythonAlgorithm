import sys
input = sys.stdin.readline

n = int(input())

home = list(map(int,input().split()))
home.sort()
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += abs(home[i]-home[len(home)//2-1])
    sum2 += abs(home[i]-home[len(home)//2])

if sum1>sum2:
    print(home[len(home)//2])
else:
    print(home[len(home)//2-1])