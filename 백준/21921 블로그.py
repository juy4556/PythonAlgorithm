if __name__ == "__main__":
    N, X = map(int, input().split())
    visitors = list(map(int, input().split()))
    start, end = 1, X
    count = 1
    _sum = result = sum(visitors[:X])

    while end <= N - 1:
        _sum = _sum - visitors[start - 1] + visitors[end]
        if result < _sum:
            result = _sum
            count = 1
        elif result == _sum:
            count += 1
        start += 1
        end += 1

    if result:
        print(result)
        print(count)
        exit()
    print("SAD")
