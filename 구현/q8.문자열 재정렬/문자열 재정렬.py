s = input()
temp = []
sum = 0
for i in range(len(s)):
    if ord(s[i]) >= 65:
        temp.append((s[i]))
    else:
        sum += int(s[i])
temp.sort()
temp.append(sum)
for i in range(len(temp)):
    print(temp[i], end='')