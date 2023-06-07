import sys

input = sys.stdin.readline


def bin_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    arr = [0]

    for num in A:
        if num > arr[-1]:
            arr.append(num)
            continue
        arr[bin_search(num, 1, len(arr) - 1)] = num

    print(len(arr) - 1)
