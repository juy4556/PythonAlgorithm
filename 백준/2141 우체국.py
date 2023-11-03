import bisect
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    pos = []
    for _ in range(N):
        X, A = map(int, input().split())
        pos.append((X, A))
    pos.sort()
    start = -int(1e9)
    end = int(1e9)
    best_pos = [int(1e10), 0]  # total_dist_diff, position
    while start <= end:
        mid = (start + end) // 2
        total_dist1 = 0
        total_dist2 = 0
        for x, a in pos:
            total_dist1 += abs(mid - x) * a
            total_dist2 += abs(mid + 1 - x) * a
        if total_dist1 <= total_dist2:
            end = mid - 1
        else:
            start = mid + 1

    idx = bisect.bisect_left(pos, (start,))
    print(pos[idx][0])
