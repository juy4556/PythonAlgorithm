if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    result = [-1] * N
    arr = []

    for i in range(N):
        while arr and A[arr[-1]] < A[i]:
            result[arr.pop()] = A[i]
        arr.append(i)

    print(*result)
