n = int(input())
alphabet = list((input().split()))

for i in range(len(alphabet)):
    alphabet[i] = ord(alphabet[i]) - 65

index = 0
count = 0
while index < n:
    if alphabet[index] != index:
        idx = alphabet.index(index)
        if idx > index:
            alphabet[idx], alphabet[idx-1] = alphabet[idx-1], alphabet[idx]
        elif idx < index:
            alphabet[idx], alphabet[idx+1] = alphabet[idx+1], alphabet[idx]
        count += 1
        continue
    index += 1

print(count)
