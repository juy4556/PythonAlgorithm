import sys

input = sys.stdin.readline


def find_graph(start, num_set):
    if start in num_set or visited[start]:
        return start
    num_set.add(start)
    return find_graph(nums[start], num_set)


if __name__ == "__main__":
    N = int(input())
    parent = [i for i in range(N + 1)]
    result = []
    nums = [0]
    visited = [0 for i in range(N + 1)]
    visited[0] = 1
    for i in range(1, N + 1):
        nums.append(int(input()))

    for i in range(1, N + 1):
        num_set = set()
        if find_graph(i, num_set) == i:
            for num in num_set:
                result.append(num)
                visited[num] = 1

    print(len(result))
    for num in sorted(result):
        print(num)
