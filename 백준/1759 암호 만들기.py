import sys

input = sys.stdin.readline


def dfs(pwd, start):
    if len(pwd) == L:
        vowel_count = 0
        for char in pwd:
            if char in vowel:
                vowel_count += 1
        if vowel_count >= 1 and L - vowel_count >= 2:
            print(pwd)
        return
    for i in range(start, C):
        pwd += chars[i]
        dfs(pwd, i + 1)
        pwd = pwd[:-1]


if __name__ == "__main__":
    L, C = map(int, input().split())
    chars = list(input().rstrip().split())
    chars.sort()
    vowel = {'a', 'e', 'i', 'o', 'u'}
    dfs('', 0)
