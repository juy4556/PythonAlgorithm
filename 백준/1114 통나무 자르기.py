def cut(length):
    if length < longest_interval:
        return 10001, 0
    cut_count = 0
    cur_pos = 0
    for itv in interval:
        cur_pos += itv
        if cur_pos > length:
            cut_count += 1
            cur_pos = itv

    if cut_count != C:
        cur_pos = interval[-1]
    return cut_count, cur_pos


def bin_search(start, end):
    longest, cutting_point = 1000000001, 0
    while start <= end:
        mid = (start + end) // 2
        count, pos = cut(mid)
        if count <= C:
            longest = mid
            cutting_point = pos
            end = mid - 1
        else:
            start = mid + 1

    return longest, cutting_point


if __name__ == "__main__":
    L, K, C = map(int, input().split())
    pos = [0] + list(map(int, input().split())) + [L]
    pos.sort()
    interval = [pos[i] - pos[i - 1] for i in range(len(pos) - 1, 0, -1)]
    longest_interval = max(interval)
    print(*bin_search(1, L))
