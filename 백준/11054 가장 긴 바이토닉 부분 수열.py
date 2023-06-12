if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = A[::-1]
    dp1 = [0 for _ in range(N)]
    dp2 = [0 for _ in range(N)]
    dp1[0] = 1
    dp2[0] = 1
    result = 0

    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                dp1[i] = max(dp1[i], dp1[j] + 1)

            if B[i] > B[j]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
        if dp1[i] == 0:
            dp1[i] = 1
        if dp2[i] == 0:
            dp2[i] = 1

    for i in range(N):
        result = max(result, dp1[i] + dp2[N - 1 - i])

    print(result - 1)
