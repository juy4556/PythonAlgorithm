def possible(answer):
    for x, y, a in answer:
        if a == 0: # 기둥일때
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:                    continue
            return False
        elif a == 1: # 보일때
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:# 삭제일때
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
        elif b == 1: # 설치일때
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])

    return sorted(answer)