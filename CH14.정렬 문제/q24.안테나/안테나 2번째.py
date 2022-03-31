n = int(input())
position = list(map(int, input().split()))

position.sort()
sum1, sum2 = 0, 0
for i in range(len(position)):
    sum1 += abs(position[i] - position[len(position)//2-1])
    sum2 += abs(position[i] - position[len(position)//2])

if sum1 <= sum2:
    print(position[len(position)//2-1])
else:
    print(position[len(position) // 2])