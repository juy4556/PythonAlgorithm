from collections import defaultdict


def calculateDays(date):
    year, month, day = date.split('.')
    return int(year) * 12 * 28 + int(month) * 28 + int(day)


def solution(today, terms, privacies):
    dic = defaultdict(int)
    answer = []

    for i in range(len(terms)):
        ch, num = terms[i].split(' ')
        dic[ch] = 28 * int(num)

    today_days = calculateDays(today)
    for i in range(len(privacies)):
        date, ch = privacies[i].split(' ')
        if today_days > calculateDays(date) + dic[ch] - 1:
            answer.append(i + 1)
    return answer


print(solution("2020.01.01", ["A 6", "B 12", "C 13", "Z 3", "D 5"],
               ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
