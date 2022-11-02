queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
# queue1 = [3, 2, 7, 2]
# queue2 = [4, 6, 5, 1]

# def solution(queue1, queue2):
#     answer = 1e9
#     queue = queue1 + queue2 + queue1 + queue2
#     for i in range(len(queue)):
#         for j in range(i + 1, len(queue) + 1):
#             if j - i + 1 > len(queue1 + queue2) - 1:
#                 continue
#             if sum(queue[i:j]) == sum(queue[j:j + len(queue1) + len(queue2) - (j - i)]):
#                 answer = min(answer, i + (j - 4) % len(queue1))
#     if answer == 1e9:
#         answer = -1
#     return answer
from collections import deque
def solution(queue1, queue2):
    answer = -1
    cnt = 0
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    total_sum = sum_q1 + sum_q2
    if total_sum % 2:
        return answer
    count = 1
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    half_sum = total_sum / 2
    limit = len(queue1)*3
    while True:
        if count > limit:
            break
        if sum_q1 > half_sum:
            n = queue1.popleft()
            queue2.append(n)
            sum_q1 -= n
            sum_q2 += n
            cnt += 1
        elif sum_q2 > half_sum:
            n = queue2.popleft()
            queue1.append(n)
            sum_q1 += n
            sum_q2 -= n
            cnt += 1
        else:
            answer = cnt
            return answer
        count += 1
    return answer


print(solution(queue1, queue2))