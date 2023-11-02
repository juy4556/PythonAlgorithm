import sys

input = sys.stdin.readline
if __name__ == "__main__":
    S = input().rstrip()
    bomb = list(input().rstrip())
    bl = len(bomb)
    s = []
    for i in range(len(S)):
        s.append(S[i])
        sl = len(s)
        if sl >= bl and s[-1] == bomb[-1]:
            flag = 0
            for j in range(sl - 1, sl - 1 - bl, -1):
                if s[j] != bomb[bl - 1 - (sl - 1 - j)]:
                    flag = 1
                    break
            if not flag:
                for _ in range(bl):
                    s.pop()

    if len(s):
        print("".join(s))
    else:
        print("FRULA")
