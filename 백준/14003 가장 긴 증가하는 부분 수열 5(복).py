from bisect import bisect_left

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    arr = [-1000000001]  # 가장 긴 부분 수열 길이를 위한 리스트
    log = [(-1, -1000000001)]  # arr에 add, update 로그를 담은 리스트
    result = []

    for i in range(N):
        if arr[-1] < A[i]:
            arr.append(A[i])
            log.append((len(arr) - 1, A[i]))
            continue
        index = bisect_left(arr, A[i])
        arr[index] = A[i]
        log.append((index, A[i]))

    length = len(arr) - 1
    for i in range(N, 0, -1):
        idx, num = log[i]
        if idx == length:
            result.append(num)
            length -= 1

    print(len(arr) - 1)
    print(*result[::-1])
