import math
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = N
temp = []
for a in A:
    a = a - B
    if a > 0:
        temp.append(math.ceil(a / C))
    else:
        temp.append(0)

result += sum(temp)

print(result)