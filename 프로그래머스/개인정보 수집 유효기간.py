from collections import defaultdict


def calculate_days(year, month, day):
    days = (int(year) - 2000) * 12 * 28 + int(month) * 28 + int(day)
    return days


def solution(today, terms, privacies):
    answer = []
    year, month, day = today.split(".")
    today = calculate_days(year, month, day)
    dic = defaultdict()
    for i in range(len(terms)):
        kind, months = terms[i].split()
        dic[kind] = int(months)

    for i in range(len(privacies)):
        date, kind = privacies[i].split()
        year, month, day = date.split('.')
        days = calculate_days(year, month, day)
        days += dic[kind] * 28
        print(days, today)
        if days <= today:
            answer.append(i + 1)

    return answer


res = solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])

print(res)
