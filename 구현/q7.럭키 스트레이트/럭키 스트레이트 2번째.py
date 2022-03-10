n = int(input())
num = [-1] * len(str(n))
for i in range(len(str(n))):
    num[i] = (n % 10)
    if n / 10 > 0:
        n //= 10
sum1, sum2 = 0, 0
for i in range(len(num)//2):
    sum1 += num[i]

for i in range(len(num)//2, len(num)):
    sum2 += num[i]

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")