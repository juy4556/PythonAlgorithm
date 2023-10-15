if __name__ == "__main__":
    while True:
        num = list(map(int, input().split()))
        num.sort()
        if num[-1] != 0 and num[-1] >= num[0] + num[1]:
            print("Invalid")
            continue
        elif num[-1] == 0:
            break
        a, b, c = num

        dic = {}
        dic[a] = 0
        dic[b] = 0
        dic[c] = 0
        dic[a] += 1
        dic[b] += 1
        dic[c] += 1
        count = 0

        for v in dic.values():
            count = max(count, v)
        if count == 3:
            print("Equilateral")
        elif count == 2:
            print("Isosceles")
        else:
            print("Scalene")
