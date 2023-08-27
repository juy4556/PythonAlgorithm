import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    is_prime = [0, 0] + [1] * (N - 1)
    prime = [0]
    result = 0
    for n in range(2, N + 1):
        if is_prime[n]:
            prime.append(prime[-1] + n)

            j = 2
            while n * j <= N:
                is_prime[n * j] = 0
                j += 1

    pl = len(prime)
    start, end = 0, 1
    _sum = 0
    while start <= end < pl:
        _sum = prime[end] - prime[start]
        if _sum < N:
            end += 1
        elif _sum > N:
            start += 1
        else:
            result += 1
            start += 1
            end += 1

    print(result)
