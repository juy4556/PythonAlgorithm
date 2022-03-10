n, m = map(int, input().split()) # n은 볼링공 수, m은 공 최대 무게 n은 1이상 1000이하, m은 1이상 10이하
ball = [0] * (m+1)
weight = list(map(int, input().split()))

for i in range(n):
    ball[weight[i]] += 1
result = 0
for i in range(1, m + 1):
    n -= ball[i]
    result += ball[i] * n

print(result)
