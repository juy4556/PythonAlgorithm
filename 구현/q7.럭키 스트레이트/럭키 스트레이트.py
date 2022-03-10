n = int(input())
num = []
i = 0
while True:
    num.append(n % 10)
    if not(n // 10):
        break
    n //= 10

sum1 = 0
sum2 = 0

for i in range(len(num)//2):
    sum1 += num[i]

for i in range(len(num)//2, len(num)):
    sum2 += num[i]

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
