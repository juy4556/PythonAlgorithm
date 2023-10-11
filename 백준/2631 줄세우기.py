if __name__ == "__main__":
    N = int(input())
    arr = []
    dp = [1 for _ in range(N)]

    for i in range(N):
        arr.append(int(input()))

    for i in range(1, N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(N - max(dp))
