if __name__ == "__main__":
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    sub_sum = arr[0]
    start, end = 0, 1
    result = 100001
    while start < end <= N:
        while end < N and sub_sum < S:
            sub_sum += arr[end]
            end += 1
        if sub_sum >= S:
            result = min(result, end - start)
        sub_sum -= arr[start]
        start += 1

    if result == 100001:
        print(0)
    else:
        print(result)
