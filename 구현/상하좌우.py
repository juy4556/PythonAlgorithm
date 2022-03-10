n = int(input())
move = list((input().split()))
x = 1
y = 1
direction = ['L','R','U','D']

for i in range(len(move)):
    if move[i]==direction[0]:
        if y > 1:
            y -= 1
    elif move[i]==direction[1]:
        if y < 5:
            y += 1
    elif move[i]==direction[2]:
        if x > 1:
            x -= 1
    else:
        if x < 5:
            x += 1

print(x, y)