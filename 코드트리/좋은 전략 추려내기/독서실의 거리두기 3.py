N = int(input())
str = input()
count = []
start, end = 0, 1
while start < N and end < N:
    while end < N and str[end] == '0':
        end += 1
    count.append(end - start - 1)
    start = end
    end += 1
count.sort()
if count[len(count) - 1] % 2 == 0:
    count[len(count) - 1] = count[len(count) - 1] // 2 - 1
else:
    count[len(count) - 1] = count[len(count) - 1] // 2
print(min(count) + 1)
