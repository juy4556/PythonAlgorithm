import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    liquids = list(map(int, input().split()))
    liquids.sort()
    l1, l2, l3 = 0, 1, N - 1
    minimum = abs(liquids[0] + liquids[1] + liquids[-1])
    for i in range(N - 2):
        now = liquids[i]
        start, end = i + 1, N - 1
        while start < end:
            mix = now + liquids[start] + liquids[end]
            if abs(mix) < minimum:
                l1, l2, l3 = i, start, end
                minimum = abs(mix)

            if mix < 0:
                start += 1
            elif mix > 0:
                end -= 1
            else:
                print(liquids[l1], liquids[l2], liquids[l3])
                exit()
    print(liquids[l1], liquids[l2], liquids[l3])
