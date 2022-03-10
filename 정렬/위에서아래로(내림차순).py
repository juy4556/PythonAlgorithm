n = int(input()) # 수의 개수 n
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
print(arr)
