from collections import defaultdict

dic = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
       5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
dic2 = defaultdict()


def solution(s):
    answer = ""
    for i in range(len(s) - 1):
        if '0' <= s[i] <= '9':
            answer += s[i]
        else:
            for j in range(0, 10):
                num = dic[j]
                if s[i:i + len(num)] == num:
                    answer += str(j)
                    break
    return int(answer)
