candidates = []


def check(array, banned_id):
    count = 0

    for arr in array:
        flag = False
        for i in range(len(arr)):
            if len(arr) != len(banned_id):
                break
            if len(arr[i]) != len(banned_id[i]):
                break
            flag2 = False
            for j in range(len(arr[i])):
                if banned_id[i][j] == '*':
                    continue
                if banned_id[i][j] != arr[i][j]:
                    flag2 = True  # 후보 문자열과 banned_id가 다름
                    break
            if flag2:  # banned_id와 동일한 리스트인 경우
                flag = False
                break
            else:
                flag = True

        if flag:
            count += 1

    return count


def dfs(arr, begin, user_id, banned_id, visited):
    if len(arr) == len(banned_id):
        candidates.append(sorted(arr))
        return
    for i in range(begin, len(user_id)):
        arr.append(user_id[i])
        dfs(arr, i + 1, user_id, banned_id, visited)
        arr.pop()


def solution(user_id, banned_id):
    global candidates
    banned_id = sorted(banned_id)
    answer = 0
    visited = [0] * len(user_id)
    dfs([], 0, user_id, banned_id, visited)
    print(check(candidates, banned_id))
    return answer


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
