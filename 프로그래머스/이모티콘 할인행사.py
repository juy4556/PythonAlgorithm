def check(temp):
    global answer
    if answer[0] < temp[0]:
        answer = temp
        return answer
    if answer[0] == temp[0]:
        if answer[1] < temp[1]:
            answer = temp
            return answer
    return answer


def calculate(discount_ratios, emoticons, users):
    emoticon_plus, total = 0, 0

    for i in range(len(users)):
        discount, limit_price = users[i]
        buy = 0
        for j in range(len(emoticons)):
            if discount <= discount_ratios[j]:
                buy += (1 - discount_ratios[j] / 100) * emoticons[j]
        if discount_ratios == [40, 27, 32, 40]:
            print(users[i], discount_ratios, buy)
        if buy >= limit_price:
            buy = 0
            emoticon_plus += 1

        total += buy
    return [emoticon_plus, total]


def dfs(arr, discounts, emoticons, users):
    global answer
    if len(arr) == len(emoticons):
        answer = check(calculate(arr, emoticons, users))
        return
    for i in discounts:
        arr.append(i)
        dfs(arr, discounts, emoticons, users)
        arr.pop()


def solution(users, emoticons):
    global answer
    answer = [0, 0]
    discounts = [10, 20, 30, 40]

    dfs([], discounts, emoticons, users)
    return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
               [1300, 1500, 1600, 4900]))
