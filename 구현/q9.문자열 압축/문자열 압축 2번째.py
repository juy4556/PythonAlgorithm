s = input()
answer = len(s)
for i in range(1, len(s)//2+1):
    compress = ""
    count = 1
    a = s[0:i]
    for j in range(i, len(s), i):
        if s[j:j+i] == a:
            count += 1
        else:
            compress += str(count)+a if count >=2 else a
            count = 1
            a = s[j:j+i]
    compress += str(count)+a if count >= 2 else a
    print(compress)
    answer = min(answer, len(compress))

print(answer)