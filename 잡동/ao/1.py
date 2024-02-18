def solution(friends, gifts):
    answer = 0
    friend_count = len(friends)
    index = dict()
    graph = [[0] * friend_count for _ in range(friend_count)]
    gift_score = [[0, 0] for _ in range(friend_count)]
    next_month = dict()
    visited = [[False] * friend_count for _ in range(friend_count)]

    for i in range(friend_count):
        index[friends[i]] = i
        next_month[friends[i]] = 0
        visited[i][i] = True

    for gift in gifts:
        gave, received = map(str, gift.split())
        graph[index[gave]][index[received]] += 1
        gift_score[index[gave]][0] += 1
        gift_score[index[received]][1] += 1

    print(graph)
    print(gift_score)

    for i in range(friend_count):
        for j in range(friend_count):
            # A는 friends[i], B는 friends[j], A -> B는 graph[i][j], B -> A는 graph[j][i]
            if not visited[i][j]:
                a = graph[i][j]
                b = graph[j][i]
                if a > b:
                    next_month[friends[i]] += 1
                elif a < b:
                    next_month[friends[j]] += 1
                else:
                    # A의 선물지수는 gift_score[i][0] - gift_score[i][0]
                    # B의 선물지수는 gift_score[j][0] - gift_score[j][0]
                    a_score = gift_score[i][0] - gift_score[i][1]
                    b_score = gift_score[j][0] - gift_score[j][1]

                    if a_score > b_score:
                        next_month[friends[i]] += 1
                    elif a_score < b_score:
                        next_month[friends[j]] += 1
                visited[i][j] = 1
                visited[j][i] = 1

    answer = max(next_month.values())
    return answer
