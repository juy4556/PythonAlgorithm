import sys
input = sys.stdin.readline

s = input().rstrip()
result = int(s[0])
for i in range(1, len(s)):
    if result == 0 or int(s[i]) == 0:
        result += int(s[i])
    else:
        result *= int(s[i])
print(result)
