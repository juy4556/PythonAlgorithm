'''
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4))
'''
'''
# 메모이제이션과 재귀함수를 활용한 구현, 큰 문제를 해결하기 위해 작은 문제를 호출 : 탑다운 방식
f = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if f[x] != 0:
        return f[x]
    f[x] = fibo(x-1) + fibo(x-2)
    return f[x]

print(fibo(99))
'''

# 피보나치수열의 반복문을 활용한 바텀업 방식, 바텀업 방식은 일반적인 다이나믹프로그래밍 형태
d = [0] * 100

d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]

print(d[n])

