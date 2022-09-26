def find_last(dl, pl, deliveries, pickups):
    while dl >= 0:
        if deliveries[dl] == 0:
            dl -= 1
        else:
            break
    while pl >= 0:
        if pickups[pl] == 0:
            pl -= 1
        else:
            break

    return dl, pl


def solution(cap, n, deliveries, pickups):
    answer = 0
    dl = n - 1
    pl = n - 1

    while dl >= 0 or pl >= 0:
        dl, pl = find_last(dl, pl, deliveries, pickups)
        answer += (max(dl, pl) + 1) * 2
        box = cap

        while dl >= 0 and box > 0:
            if deliveries[dl] == 0:
                dl -= 1
            elif deliveries[dl] <= box:
                box -= deliveries[dl]
                deliveries[dl] = 0
                dl -= 1
            else:
                deliveries[dl] -= box
                break

        pbox = cap
        while pl >= 0 and pbox > 0:
            if pickups[pl] == 0:
                pl -= 1
            elif pickups[pl] <= pbox:
                pbox -= pickups[pl]
                pickups[pl] = 0
                pl -= 1
            else:
                pickups[pl] -= pbox
                break

    return answer