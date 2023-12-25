import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N, M, K = map(int, input().split())
    referees = list(map(int, input().split()))
    start = 1
    end = referees[-1] - referees[0]
    result = '1'
    while start <= end:
        mid = (start + end) // 2
        count = 1
        prev = referees[0]
        for i in range(1, K):
            if referees[i] - prev >= mid:
                count += 1
                prev = referees[i]
        if count >= M:
            start = mid + 1
        else:
            end = mid - 1

    max_dist = end
    prev = referees[0]
    count = 1
    for i in range(1, K):
        if referees[i] - prev >= max_dist and count < M:
            result += '1'
            count += 1
            prev = referees[i]
        else:
            result += '0'

    print(result)
