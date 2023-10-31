import sys

input = sys.stdin.readline


def count_one(num):
    bin_num = bin(num)[2:]
    length = len(bin_num)
    count = 0
    for i in bin_num:
        if i == '1':
            count += one_count[length - 1]
            # 맨 앞자리 카운트
            count += num - 2 ** (length - 1) + 1
            num -= 2 ** (length - 1)
        length -= 1
    return count


if __name__ == "__main__":
    A, B = map(int, input().split())
    one_count = [0 for _ in range(55)]  # 10^16이 2^54보다 작음

    for i in range(1, 55):
        one_count[i] = i * 2 ** (i - 1)

    print(count_one(B) - count_one(A - 1))
