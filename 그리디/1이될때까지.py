n, k = map(int, input().split())
count = 0
while 1:
    target = (n//k) * k
    remain = n - target
    count += remain
    n = target
    if n == 0:
        break
    n = n // k
    count += 1

count -= 1
print(count)