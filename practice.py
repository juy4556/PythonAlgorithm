move_priority = [[] for _ in range(4)]
for i in range(4):
    for j in range(4):
        s = list(map(int, input().split()))
        move_priority[i].append(s)
print(move_priority)