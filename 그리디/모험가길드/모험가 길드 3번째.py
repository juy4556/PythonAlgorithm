n = int(input())
array = list(map(int, input().split()))

array.sort()

result = 0
cnt = 0
for i in array:
    cnt += 1
    if cnt >= i:
        cnt = 0
        result += 1

print(result)