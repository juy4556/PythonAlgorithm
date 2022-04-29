from collections import deque

result = 0


def isPrime(num):
    if num == 0 or num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def permutation(pieces, perm, level, r, visited, masterpiece):
    global result
    if level == r:
        perm = ''.join(perm)
        if isPrime(int(perm)) and int(perm) not in masterpiece:
            masterpiece.append(int(perm))
            result += 1
        return
    for i in range(len(pieces)):
        if visited[i] == True:
            continue
        visited[i] = True
        perm.append(pieces[i])
        permutation(pieces, perm, level + 1, r, visited, masterpiece)
        perm.pop()
        visited[i] = False


def solution():
    global result
    c = int(input())
    for _ in range(c):
        result = 0
        perm = deque()
        pieces = input()
        masterpiece = []
        for i in range(1, len(pieces) + 1):
            visited = [False] * len(pieces)
            permutation(pieces, perm, 0, i, visited, masterpiece)
        print(result)


solution()
