n, m = map(int, input().split())
num = []
arr = [[]]
for _ in range(n):
    num.append(int(input()))

index = 0
for n in num:
    if sum(arr[index]) + len(arr[index]) + n > m:
        index += 1
        arr.append([n])
    else:
        arr[index].append(n)

for i in range(1, len(arr)):
