import random

std = 1000
num = [0] * 10001
cnt = 0
for i in range(10000):
    num[random.randint(0, 10000)] += 1

while True:
    cnt = 0
    for i in range(std, 10000):
        cnt += num[i]

    if cnt > std:
        std += 1000
        cnt += 1
    else:
        break

print(cnt)