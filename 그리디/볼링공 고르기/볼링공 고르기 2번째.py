n, m = map(int, input().split())
ball = [0] * 11
weight = list(map(int, input().split()))
for i in weight:
    ball[i] += 1

result = 0
for i in range(1, 11):
    result += (n-ball[i]) * ball[i]
    n -= ball[i]

print(result)