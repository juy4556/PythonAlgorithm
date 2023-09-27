import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [0 for _ in range(100001)]
    left, right = 0, 0
    count = 0
    while left <= right < N:
        while visited[arr[right]]:
            visited[arr[left]] = 0
            left += 1

        if not visited[arr[right]]:
            visited[arr[right]] = 1
            right += 1
            count += right - left

    print(count)
