N, M = map(int, input().split())
A = list(map(int, input().split()))
arr = [0] * N
sub_sum = 0
rest = [0] * 1000
result = 0

for i in range(N):
    sub_sum += A[i]
    arr[i] = sub_sum
    rest[arr[i] % M] += 1

result += rest[0]
for i in range(M):
    if rest[i] > 1:
        result += rest[i] * (rest[i] - 1) // 2
print(result)
