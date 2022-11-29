n = int(input())
a, b = 0, 0
condition = 0  # -1 : a가 더 클 때,0 : a,b값 같을 때, 1 : b가 더 클 때
count = 0
for _ in range(n):
    c, s = input().split()
    if c == "A":
        a += int(s)
    elif c == "B":
        b += int(s)
    cond = condition
    if a > b:
        condition = 1
    elif a < b:
        condition = -1
    else:
        condition = 0

    if cond != condition:
        count += 1

print(count)
