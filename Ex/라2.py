from typing import List

def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''
    chats = chat.split(' ')
    for badword in dic:
        if badword


    for word in chats:
        if '.' in word:
            for index in range(len(word)):
                temp = word
                if word[index] == '.':
                    for i in range(97, 123):
                        temp = word[:index]+chr(i)+word[index+1]
                        word.replace('.', chr(i))
                        print(chr(i))

        if word in dic:
            answer += '#'*len(word)+' '
        else:
            answer += word+' '
    print(chats)
    return answer


print(solution(2,["slang","badword"],"badword ab.cd bad.ord .word sl.. bad.word"))
