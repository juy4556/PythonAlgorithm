import sys

input = sys.stdin.readline

n = int(input())  # 50000이하
carriage = list(map(int, input().split()))  # 객차에 타고 있는 손님 수
limit = int(input())  # 소형 기관차가 최대로 끌 수 있는 객차 수

dp = [[0] * (n + 1) for _ in range(4)]
S = [0]
summary = 0
for c in carriage:
    summary += c
    S.append(summary)

for i in range(1, 4):
    for j in range(i * limit, n + 1):
        if i == 1:
            dp[i][j] = max(dp[i][j - 1], S[j] - S[j - limit])
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - limit] + S[j] - S[j - limit])

print(dp[3][n])
