from collections import deque


def combination_algorithm(array, comb, level, r, begin, visited):
    if level == r:
        print(list(comb))
        return comb
    for i in range(begin, len(array)):
        comb.append(array[i])
        combination_algorithm(array, comb, level + 1, r, i + 1, visited)
        comb.pop()


def solution():
    arr = [1, 4, 7, 3, 2, 6]
    comb = deque()
    visited = [False] * len(arr)

    for i in range(1, len(arr) + 1):  # i는 조합의 크기
        combination_algorithm(arr, comb, 0, i, 0, visited)


solution()
