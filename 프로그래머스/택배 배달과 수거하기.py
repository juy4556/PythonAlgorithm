def find_last(deliveries, pickups, dl, pl):
    for i in range(dl, -1, -1):
        if deliveries[i]:
            break
        dl -= 1
    for i in range(pl, -1, -1):
        if pickups[i]:
            break
        pl -= 1
    return dl, pl


def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery_length, pickup_length = n - 1, n - 1
    while delivery_length >= 0 or pickup_length >= 0:
        delivery_length, pickup_length = find_last(deliveries, pickups, delivery_length, pickup_length)
        put = get = cap
        answer += 2 * (max(delivery_length, pickup_length) + 1)

        while delivery_length >= 0 and put:
            if deliveries[delivery_length] == 0:
                delivery_length -= 1
            elif deliveries[delivery_length] <= put:
                put -= deliveries[delivery_length]
                deliveries[delivery_length] = 0
                delivery_length -= 1
            else:
                deliveries[delivery_length] -= put
                put = 0

        while pickup_length >= 0 and get:
            if pickups[pickup_length] == 0:
                pickup_length -= 1
            elif pickups[pickup_length] <= get:
                get -= pickups[pickup_length]
                pickups[pickup_length] = 0
                pickup_length -= 1
            else:
                pickups[pickup_length] -= get
                get = 0

    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))

print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
