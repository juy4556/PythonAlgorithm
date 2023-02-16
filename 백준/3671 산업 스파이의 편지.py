from itertools import permutations


def isPrime(num):
    if num == 0 or num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def solution():
    c = int(input())
    for _ in range(c):
        already = []
        result = 0
        pieces = input()
        for i in range(1, len(pieces) + 1):
            perm = list(permutations(pieces, i))
            for p in perm:
                temp = "".join(p)
                if isPrime(int(temp)) and int(temp) not in already:
                    result += 1
                    already.append(int(temp))
        print(result)


solution()
