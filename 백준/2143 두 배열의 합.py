import bisect
import sys

input = sys.stdin.readline
if __name__ == "__main__":
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    result = 0
    a, b = A, B

    for i in range(1, n):
        A[i] += A[i - 1]
    for i in range(n - 1):
        for j in range(i + 1, n):
            a.append(A[j] - A[i])
    for i in range(1, m):
        B[i] += B[i - 1]
    for i in range(m - 1):
        for j in range(i + 1, m):
            b.append(B[j] - B[i])

    s1, e1 = 0, len(a) - 1
    s2, e2 = 0, len(b) - 1
    a.sort()
    b.sort()
    total = 0
    while s1 <= e1 and s2 <= e2:
        total = a[s1] + b[e2]
        if total == T:
            a_cnt = bisect.bisect_right(a, a[s1]) - bisect.bisect_left(a, a[s1])
            b_cnt = bisect.bisect_right(b, b[e2]) - bisect.bisect_left(b, b[e2])
            result += a_cnt * b_cnt
            s1 += a_cnt
            e2 -= b_cnt

        elif total < T:
            s1 += 1
        else:
            e2 -= 1

    print(result)
