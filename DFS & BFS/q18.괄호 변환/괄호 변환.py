def find_balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
        if count < 0:
            return False
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = find_balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

s = input()
print(solution(s))