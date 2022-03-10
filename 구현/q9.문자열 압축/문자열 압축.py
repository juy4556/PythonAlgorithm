def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        compress = ""
        a = s[0:i]
        count = 1
        print(a)
        for j in range(i, len(s), i):
            if a == s[j:j+i]:
                count += 1
            else: # 다른 문자열이 올 때
                compress += str(count) + a if count >= 2 else a
                count = 1
                a = s[j:j+i] # 새로운 문자열로 초기화
        compress += str(count) + a if count >= 2 else a
        answer = min(answer, len(compress))
    return answer

s = input()
print(solution(s))