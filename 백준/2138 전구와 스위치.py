import sys

input = sys.stdin.readline


def switch_on(arr, idx):
    arr[idx - 1] = not arr[idx - 1]
    arr[idx] = not arr[idx]
    if idx + 1 < N:
        arr[idx + 1] = not arr[idx + 1]


if __name__ == "__main__":
    N = int(input())
    bef = list(map(int, " ".join(input()).split()))
    aft = list(map(int, " ".join(input()).split()))

    for i in range(2):
        count = 0
        before = bef[:]
        after = aft[:]
        if i == 1:
            before[0] = not before[0]
            before[1] = not before[1]
            count += 1
        idx = 1
        while idx < N:
            if before[idx - 1] != after[idx - 1]:
                switch_on(before, idx)
                count += 1
            idx += 1

        if before[-1] == after[-1]:
            print(count)
            exit()

    print(-1)
