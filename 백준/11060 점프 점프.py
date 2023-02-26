N = int(input())
A = list(map(int, input().split()))
dp = [1001] * N
dp[0] = 0
for i in range(N):
    jump = A[i]
    for j in range(1, jump + 1):
        if i + j >= N:
            break
        dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[N - 1] < 1001:
    print(dp[N - 1])
else:
    print(-1)
