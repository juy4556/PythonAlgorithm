from collections import deque


def solution(coin, cards):
    cards_length = len(cards)
    q = deque(cards[cards_length // 3:])
    now = cards[:cards_length // 3]
    now.sort()
    goal = cards_length + 1
    round = 1
    discarded = []
    while q:
        a = q.popleft()
        b = q.popleft()
        discarded.append(a)
        discarded.append(b)
        now_length = len(now)
        discarded_length = len(discarded)
        # print(now, discarded, coin)
        if comb_cards(goal, now_length, now):
            round += 1
            continue

        if coin >= 1 and comb_now_and_discarded(discarded, goal, now):
            round += 1
            coin -= 1
            continue

        if coin >= 2 and comb_cards(goal, discarded_length, discarded):
            round += 1
            coin -= 2
            continue

        break
    return round


def comb_now_and_discarded(discarded, goal, now):
    ended = False
    now_length = len(now)
    discarded_length = len(discarded)
    for i in range(now_length):
        for j in range(discarded_length):
            if now[i] + discarded[j] == goal:
                ended = True
                now.pop(i)
                discarded.pop(j)
                return ended

    return ended


def comb_cards(goal, length, num):
    ended = False
    if length >= 2:
        for i in range(length - 1):
            for j in range(i + 1, length):
                if num[i] + num[j] == goal:
                    num.pop(j)
                    num.pop(i)
                    ended = True
                    return ended

    return ended


print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))  # 5
print(solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]))  # 2
print(solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]))  # 4
print(solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))  # 1
