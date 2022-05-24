H, W = map(int, input().split())
height = list(map(int, input().split()))
count = 0
for h in range(1, H+1):
    temp = []
    for i in range(len(height)):
        if height[i] >= h:
            temp.append(i)
    if len(temp) > 1:
        for j in range(1, len(temp)):
            count += temp[j]-temp[j-1]-1
print(count)