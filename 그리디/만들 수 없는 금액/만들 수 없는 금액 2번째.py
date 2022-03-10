n = int(input())
currency = list(map(int, input().split()))
currency.sort()

target = 1
for i in currency:
    if target < i:
        break
    target += i

print(target)