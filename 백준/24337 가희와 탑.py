import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N, a, b = map(int, input().split())
    if a + b - 1 > N:
        print(-1)
    else:
        arr1 = [i + 1 for i in range(a - 1)]
        arr2 = [i + 1 for i in range(b - 1)]
        if a >= b:
            arr1.append(a)
        else:
            arr2.append(b)
        arr = arr1 + list(reversed(arr2))

        while len(arr) < N:
            arr.insert(1, 1)

        print(*arr)
