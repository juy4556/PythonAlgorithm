N, M = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))
T.sort()

start, end = 0, max(T) * M
result = end
while start <= end:
    mid = (start+end) // 2
    count = 0
    for t in T:
        count += mid // t

    if count >= M:
        end = mid - 1
        result = mid
    elif count < M:
        start = mid + 1

print(result)