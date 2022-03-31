def isrightstring(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
        if count < 0:
            return False
    return True

def solution(p):
    answer = ""
    if p == "":
        return answer
    cnt1 = 0  # '('수
    cnt2 = 0  # ')'수
    u = ""
    v = ""
    for i in range(len(p)):
        if p[i] == '(':
            cnt1 += 1
        elif p[i] == ')':
            cnt2 += 1
        if cnt1 == cnt2:
            u = p[:i + 1]
            v = p[i + 1:]
            break
    if isrightstring(u):
        answer = u + solution(v)

    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])  # 맨앞뒤 자르기
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            elif u[i] == ')':
                u[i] = '('
        answer += "".join(u)

    return answer

s = input()
print(solution(s))