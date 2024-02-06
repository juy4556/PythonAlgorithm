import sys

input = sys.stdin.readline


def is_palindrome(s):
    mid = len(s) // 2
    if len(s) & 1:
        index = 1
        while mid - index >= 0 and s[mid - index] == s[mid + index]:
            index += 1
        if index <= mid:
            return False
    else:
        index = 0
        while mid - 1 - index >= 0 and s[mid + index] == s[mid - 1 - index]:
            index += 1
        if index <= mid - 1:
            return False
    return True


if __name__ == "__main__":
    S = input().strip()
    s_len = len(S)
    index = 0
    result = 0
    for i in range(s_len):
        if is_palindrome(S[i:]):
            result += s_len - i
            index = i
            break
    result += 2 * index
    print(result)
