N = int(input())
dp = [0] * (N+1)
T=[]
P=[]
for i in range(N-1, -1, -1):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N-1, -1, -1):
    if T[i]+i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+T[i]]+P[i], dp[i+1])
print(dp[0])