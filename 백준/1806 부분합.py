N, S = map(int, input().split())
arr = list(map(int, input().split()))

result = 100001
sub_sum = arr[0]
end = 1
for start in range(N):
    while sub_sum < S and end < N:
        sub_sum += arr[end]
        end += 1
    if end <= start:
        continue
    if sub_sum >= S:
        result = min(result, end-start)
    sub_sum -= arr[start]

if result == 100001:
    print(0)
else:
    print(result)