from collections import deque


def permutation_algorithm(array, perm, n, r, visited):
    if n == r:
        print(list(perm))
        return perm
    for i in range(len(array)):
        if visited[i] == True:
            continue
        visited[i] = True
        perm.append(array[i])
        permutation_algorithm(array, perm, n + 1, r, visited)
        perm.pop()
        visited[i] = False


def solution():
    arr = [1, 4, 7, 3, 2, 6]
    perm = deque()
    visited = [False] * len(arr)

    for i in range(1, len(arr) + 1):  # i는 순열의 크기
        permutation_algorithm(arr, perm, 0, i, visited)

solution()