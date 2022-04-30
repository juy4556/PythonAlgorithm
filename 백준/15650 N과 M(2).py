N, M = map(int, input().split())
comb = []


def solution(begin):
    if len(comb) == M:
        print(*comb)
        return
    for i in range(begin, N + 1):
        comb.append(i)
        solution(i + 1)
        comb.pop()


solution(1)