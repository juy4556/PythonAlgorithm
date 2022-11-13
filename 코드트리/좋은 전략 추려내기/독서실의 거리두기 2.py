N = int(input())
str = input()
start, end = 0, 1
position = [0]
answer = []

for i in range(len(str)):
    if str[i] == '1':
        position.append(i)
position.append(len(str)-1)
answer.append(position[1]-position[0])
answer.append(position[len(position)-1]-position[len(position)-2])

widest = 0
index = 0
for i in range(len(position)-1):
    if widest < position[i+1]-position[i]:
        widest = position[i+1]-position[i]
        index = i

new = position[index] + (position[index+1] - position[index]) // 2
position.append(new)
position.sort()

result = 1001
for i in range(1, len(position)-2):
    if result > position[i+1] - position[i]:
        result = position[i+1] - position[i]
answer.append(result)

result = 1001
if max(answer) == answer[0]:
    position.remove(new)
    for i in range(len(position) - 2):
        if result > position[i + 1] - position[i]:
            result = position[i + 1] - position[i]
elif max(answer) == answer[1]:
    position.remove(new)
    for i in range(1, len(position)-1):
        if result > position[i + 1] - position[i]:
            result = position[i + 1] - position[i]
else:
    for i in range(1, len(position)-2):
        if result > position[i+1] - position[i]:
            result = position[i+1] - position[i]
print(result)
