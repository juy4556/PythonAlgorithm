import sys
s = sys.stdin.readline().rstrip()
token = [0] * 2 # 0이 나열된 집합 수, 1일 나열된 집합 수

if int(s[0]) == 0:
    token[0] += 1
else:
    token[1] += 1

for i in range(len(s)-1):
    if int(s[i]) != int(s[i+1]):
        token[int(s[i+1])] += 1

print(min(token[0], token[1]))