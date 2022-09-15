N = int(input())
arr = []
maximum, minimum = 0, 0
first = list(map(int, input().split()))
maxdp=first
mindp=first
for i in range(1, N):
    a, b, c = map(int, input().split())
    maxdp = [a+max(maxdp[0],maxdp[1]), b+max(maxdp[0],max(maxdp[1],maxdp[2])), c+max(maxdp[1], maxdp[2])]
    mindp = [a+min(mindp[0],mindp[1]), b+min(mindp[0],min(mindp[1],mindp[2])), c+min(mindp[1],mindp[2])]

print(max(maxdp),min(mindp))