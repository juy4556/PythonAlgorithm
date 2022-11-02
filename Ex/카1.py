from collections import defaultdict

dic = defaultdict(int)


def solution(survey, choices):
    answer = ''
    for i in range(len(choices)):
        if choices[i] == 4:
            continue
        elif choices[i] == 1:
            dic[survey[i][:1]] += 3
        elif choices[i] == 2:
            dic[survey[i][:1]] += 2
        elif choices[i] == 3:
            dic[survey[i][:1]] += 1
        elif choices[i] == 5:
            dic[survey[i][1:]] += 1
        elif choices[i] == 6:
            dic[survey[i][1:]] += 2
        elif choices[i] == 7:
            dic[survey[i][1:]] += 3

    if dic['R'] < dic['T']:
        answer += 'T'
    else:
        answer += 'R'
    if dic['C'] < dic['F']:
        answer += 'F'
    else:
        answer += 'C'
    if dic['J'] < dic['M']:
        answer += 'M'
    else:
        answer += 'J'
    if dic['A'] < dic['N']:
        answer += 'N'
    else:
        answer += 'A'
    print(answer)
    return answer
