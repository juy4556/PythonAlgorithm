def isPrime(num):
    if num == 0 or num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


N = int(input())
firstPrime = ['2', '3', '5', '7']
odd = ['1', '3', '5', '7', '9']


def solution(num):
    if len(num) == N:
        print("".join(num))
    for o in odd:
        num.append(o)
        if isPrime(int("".join(num))):
            solution(num)
        num.pop()


for fp in firstPrime:
    num = [fp]
    solution(num)
