if __name__ == "__main__":
    s = input()
    count = 0
    a, b = 0, 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            if s[i] == '0':
                a += 1
            elif s[i] == '1':
                b += 1
            count += 1
    if s[-1] == '0':
        a += 1
    elif s[-1] == '1':
        b += 1

    print(min(a, b))
