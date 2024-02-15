'''
n = 1
[1]
n = 2
[1, 6, 2, 7, 5, 3, 4] len:7
1 2 1 2 1 (5)
2 3
6
n = 3
[1, 12, 2, 11, 13, 3, 18, 14, 10, 19, 4, 17, 15, 9, 16, 5, 8, 6, 7] len: 19
1 2 3 2 3 2 3 2 1 (9)
2 3 5 5 2
3 5
12
n = 4
1 2 3 4 3 4 3 4 3 4 3 2 1 (13) -> 4n-3
[1, 18, 2, 17, 19, 3, 16, 30, 20, 4, 29, 31, 21, 15, 36, 32, 5, 28, 37, 22, 14, 35, 33, 6, 27, 34, 23, 13, 26, 24, 7, 12, 25, 8, 11, 9, 10]
2 3 4 7 7 7 3 2
18
n = 5
2 3 4 5 9 9 9 9 4 3 2
'''


def find_last_idx(arr, start, n):
    for i in range(start, -1, -1):
        if arr[i] == n:
            return i
    return 0


def solution(n):
    total_count = 3 * n * (n - 1) + 1
    result = [0 for _ in range(total_count)]
    num = 1
    while n:
        pattern = [1] + [i for i in range(2, n + 1)] + [2 * n - 1] * (n - 1) + [i for i in range(n - 1, 1, -1)]
        arr = result[:]
        pattern_idx = 0
        idx = result.index(0)
        start = idx
        zero_count = 0
        for i in range(start, total_count):
            if pattern_idx >= len(pattern):
                break
            if arr[i] == 0:
                zero_count += 1
            if zero_count == pattern[pattern_idx]:
                result[i] = num
                num += 1
                zero_count = 0
                pattern_idx += 1
            idx += 1

        if n == 1 and pattern_idx >= len(pattern):
            break
        zero_count = 0
        pattern_idx = 0
        end = find_last_idx(result, total_count - 1, 0)
        for i in range(end, -1, -1):
            if pattern_idx >= len(pattern):
                break
            if arr[i] == 0:
                zero_count += 1
            if zero_count == pattern[pattern_idx]:
                result[i] = num
                num += 1
                zero_count = 0
                pattern_idx += 1
        n -= 1
    print(result)


solution(4)
