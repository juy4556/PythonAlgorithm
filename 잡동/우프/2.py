def solution(str):
    while True:
        remove = find_remove(str)
        if len(remove) == 0:
            break
        for i in range(len(remove) - 1, -1, -1):
            start, end = remove[i][0], remove[i][1]
            str = str[:start] + str[end:]
    return str


def find_remove(str):
    start, end = 0, 0
    remove = []
    while start < len(str) and end < len(str):
        while end < len(str) and str[start] == str[end]:
            end += 1
        if end - start >= 2:
            remove.append([start, end])
        start = end
        end += 1
    return remove


if __name__ == "__main__":
    str = input()
    print(solution(str))
