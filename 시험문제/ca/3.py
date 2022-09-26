def user_cost_check(answer, discounts, users, emoticons):

    member = 0
    total_cost = 0

    # print("discount: ", discounts)

    for i in range(len(users)):
        user_discount, user_total_cost = users[i]
        product_total_cost = 0

        for j in range(len(emoticons)):
            if user_discount <= discounts[j]:
                product_total_cost += emoticons[j] * (100 - discounts[j]) // 100
                # print("product_total_cost:", product_total_cost)

        if user_total_cost <= product_total_cost and product_total_cost != 0:
            member += 1
        else:
            total_cost += product_total_cost
    #
    # print("member: ", member)
    # print("total_cost", total_cost)

    if answer[0] < member:
        answer = [member, total_cost]
    elif answer[0] == member:
        answer = [member, max(answer[1], total_cost)]


def discount_recursive(discounts, users, emoticons):
    global limit_discount

    if len(discounts) == len(emoticons):
        user_cost_check(discounts, users, emoticons)
        return

    for i in range(len(limit_discount)):
        discounts.append(limit_discount[i])
        discount_recursive(discounts, users, emoticons)
        discounts.pop()


def solution(users, emoticons):
    global answer, limit_discount

    answer = [0, 0]
    limit_discount = [10, 20, 30, 40]
    discount_recursive([], users, emoticons)

    return answer


if __name__ == "__main__":
    print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
    print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
                   [1300, 1500, 1600, 4900]))
