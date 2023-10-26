import sys

input = sys.stdin.readline
if __name__ == "__main__":
    s = input().rstrip()
    length = len(s)
    a_count = s.count('a')
    i = 0
    result = 1001
    while i < length:
        window = ""
        if i + a_count > length:
            window = s[i:] + s[:a_count - (length - i)]
        else:
            window = s[i:i + a_count]

        result = min(result, window.count('b'))
        i += 1
    print(result)
