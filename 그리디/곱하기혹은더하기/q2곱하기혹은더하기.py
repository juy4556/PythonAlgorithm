s=input()

result=int(s[0])

for i in range(1, len(s)):
    if int(s[i]) <= 1 or result <= 1:
        result = result+int(s[i])
    else:
        result = result*int(s[i])

print(result)