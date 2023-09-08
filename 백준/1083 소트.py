import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    S = int(input())

    for i in range(N):
        max_num = nums[i]
        max_index = i
        for j in range(i + 1, min(N, i + S + 1)):
            if max_num < nums[j]:
                max_num = nums[j]
                max_index = j
        if max_index - i <= S and max_index != i:
            nums.pop(max_index)
            nums.insert(i, max_num)
            S -= max_index - i

        if S <= 0:
            break

    print(*nums)
