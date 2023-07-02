def count_match(a, b):
    count = 0
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            break
        count += 1
    return count


if __name__ == "__main__":
    N = int(input())
    words = []
    match_length = [0] * N
    for _ in range(N):
        words.append(input())
    arr = sorted(list(enumerate(words)), key=lambda x: x[1])
    for i in range(N - 1):
        match_count = count_match(arr[i][1], arr[i + 1][1])
        match_length[arr[i][0]] = max(match_length[arr[i][0]], match_count)
        match_length[arr[i + 1][0]] = max(match_length[arr[i + 1][0]], match_count)

    maximum = max(match_length)
    first_index = 0
    max_prefix = ''

    for i in range(N):
        if match_length[i] == maximum:
            print(words[i])
            first_index = i
            max_prefix = words[i][:maximum]
            break

    for i in range(first_index + 1, N):
        if match_length[i] == maximum and words[i][:maximum] == max_prefix:
            print(words[i])
            break
