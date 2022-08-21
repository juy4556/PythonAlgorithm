invitationPairs = []
for i in range(2):
    invitationPairs.append(list(map(int, input().split())))
print(invitationPairs)


def dfs(num, idx, arr, score, graph):
    reward = 0
    if num > 2:
        return
    if num == 0:
        reward = 10
    elif num == 1:
        reward = 3
    elif num == 2:
        reward = 1

    for index in arr:
        score[idx][1] += reward
        print(index)
        if graph[index]:
            dfs(num + 1, idx, graph[index],score,graph)


def solution(invitationPairs):
    graph = [[] for _ in range(1 + invitationPairs[-1][1])]
    score = [[i, 0] for i in range(1 + invitationPairs[-1][1])]
    for invitation in invitationPairs:
        invite, invited = invitation
        graph[invite].append(invited)
    for i in range(1, 1 + invitationPairs[-1][1]):
        dfs(0, i, graph[i], score,graph)
    score.sort(key=lambda x:(-x[1], x[0]))
    print(score)
    result = []
    for i in range(3):
        if score[i][0] > 0:
            result.append(score[i][0])
    print(result)
    return result


solution(invitationPairs)
