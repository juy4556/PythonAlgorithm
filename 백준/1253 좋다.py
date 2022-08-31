N = int(input())
A = list(map(int, input().split()))
A.sort()
i, j = 0, N - 1
result = 0
index = 0

for index in range(N):
    target = A[index]
    i, j = 0, N - 1
    if i == index:
        i += 1
    if j == index:
        j -= 1
    while i < N and j >= 0:
        if i >= j:
            break
        if A[i] + A[j] == A[index]:
            result += 1
            break
        elif A[i] + A[j] < A[index]:
            i += 1
            if i == index:
                i += 1
        elif A[i] + A[j] > A[index]:
            j -= 1
            if j == index:
                j -= 1

print(result)
