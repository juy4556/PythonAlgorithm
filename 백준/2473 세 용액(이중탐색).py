import sys

input = sys.stdin.readline


def bin_search(target, start, end):
    minimum = abs(target - liquids[start])
    idx = start
    while start <= end:
        mid = (start + end) // 2
        if minimum > abs(target - liquids[mid]):
            minimum = abs(target - liquids[mid])
            idx = mid
        if liquids[mid] >= target:
            end = mid - 1
        elif liquids[mid] < target:
            start = mid + 1
    return idx


if __name__ == "__main__":
    N = int(input())
    liquids = list(map(int, input().split()))
    liquids.sort()
    l1, l2, l3 = 0, 1, N - 1
    minimum = abs(liquids[l1] + liquids[l2] + liquids[l3])
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            mix = liquids[i] + liquids[j]
            index = bin_search(-mix, j + 1, N - 1)
            result = abs(mix + liquids[index])
            if result < minimum:
                l1, l2, l3 = i, j, index
                minimum = result
            if result == 0:
                print(liquids[l1], liquids[l2], liquids[l3])
                exit()
    print(liquids[l1], liquids[l2], liquids[l3])
