N, M, L = map(int, input().split())
rest = [0] + list(map(int, input().split())) + [L]
rest.sort()
print(rest)
start = 1
end = L-1
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, len(rest)):
        count += (rest[i]-rest[i-1]) // mid
        if (rest[i]-rest[i-1]) % mid == 0:
            count -= 1

    if count <= M:
        end = mid - 1
        result = mid
    elif count > M:
        start = mid + 1

print(result)
