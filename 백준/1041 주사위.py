import sys

input = sys.stdin.readline


def dfs(n, begin, arr):
    global minimum
    if len(arr) == 2:
        minimum = min(minimum, arr[0][1] + arr[1][1])
        return
    for i in range(begin, 6):
        if i == n or i == 6 - n - 1:
            continue
        if arr and abs(6 - i - 1) == arr[0][0]:
            continue
        arr.append([i, numbers[i]])
        dfs(n, i + 1, arr)
        arr.pop()


if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, input().split()))
    three = 151
    two = 101
    one = min(numbers)
    result = 0
    if N == 1:
        print(sum(numbers) - max(numbers))
    elif N > 1:
        for n in range(3):
            up, down = numbers[n], numbers[6 - n - 1]
            arr = []
            minimum = 101
            dfs(n, 0, [])
            three = min(three, min(up, down) + minimum)
            two = min(two, minimum)
        result = 4 * three + (2 * N - 3) * 4 * two + (N ** 2 * 5 - (3 * 4 + 2 * (2 * N - 3) * 4)) * one

        print(result)
