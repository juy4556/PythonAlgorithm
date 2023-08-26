import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    x = list(map(int, input().split()))
    numbers = set(x)
    result = [0] * 1000001
    for n in x:
        for i in range(n * 2, 1000001, n):
            if i in numbers:
                result[i] -= 1
                result[n] += 1

    for num in x:
        print(result[num], end=' ')
