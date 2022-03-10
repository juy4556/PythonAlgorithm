s = input()

alphabet = []
sum = 0
for i in range(len(s)):
    if ord(s[i]) >= 65:
        alphabet.append(s[i])
    else:
        sum += int(s[i])

alphabet.sort()
alphabet.append(str(sum))
answer = ''.join(alphabet)
print(answer)