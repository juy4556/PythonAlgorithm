import sys

input = sys.stdin.readline


def dfs(s, t, s_len):
    if len(t) == s_len:
        for i in range(s_len):
            if t[i] != s[i]:
                return
        print(1)
        exit()

    if t[-1] == 'A':
        t = t[:-1]
        dfs(s, t, s_len)
        t += 'A'

    if t[0] == 'B':
        t = "".join(list(reversed(t)))
        t = t[:-1]
        dfs(s, t, s_len)


if __name__ == "__main__":
    S = input().rstrip()
    T = input().rstrip()
    dfs(S, T, len(S))
    print(0)
