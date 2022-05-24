cogwheels = []


def rotate_clockwise(cogwheel):
    temp = cogwheel.pop()
    cogwheel.insert(0, temp)
    return cogwheel


def rotate_counter_clockwise(cogwheel):
    temp = cogwheel.pop(0)
    cogwheel.append(temp)
    return cogwheel


def calculate_point():
    result = 0
    for i in range(4):
        if cogwheels[i][0] == '1':
            result += pow(2, i)
    return result


def solution():
    for _ in range(4):
        cogwheels.append(list(input()))
    K = int(input())
    for _ in range(K):
        num, dir = map(int, input().split())
        flag1, flag2, flag3 = 0, 0, 0  # flag1은 1,2번 톱니, flag2는 2,3번 톱니, flag3은 3,4번 톱니 관계
        if cogwheels[0][2] != cogwheels[1][6]:
            flag1 = 1
        if cogwheels[1][2] != cogwheels[2][6]:
            flag2 = 1
        if cogwheels[2][2] != cogwheels[3][6]:
            flag3 = 1
        if num == 1 and dir == -1:
            cogwheels[0] = rotate_counter_clockwise(cogwheels[0])
            if flag1:
                cogwheels[1] = rotate_clockwise(cogwheels[1])
                if flag2:
                    cogwheels[2] = rotate_counter_clockwise(cogwheels[2])
                    if flag3:
                        cogwheels[3] = rotate_clockwise(cogwheels[3])
        elif num == 1 and dir == 1:
            cogwheels[0] = rotate_clockwise(cogwheels[0])
            if flag1:
                cogwheels[1] = rotate_counter_clockwise(cogwheels[1])
                if flag2:
                    cogwheels[2] = rotate_clockwise(cogwheels[2])
                    if flag3:
                        cogwheels[3] = rotate_counter_clockwise(cogwheels[3])
        elif num == 2 and dir == -1:
            cogwheels[1] = rotate_counter_clockwise(cogwheels[1])
            if flag1:
                cogwheels[0] = rotate_clockwise(cogwheels[0])
            if flag2:
                cogwheels[2] = rotate_clockwise(cogwheels[2])
                if flag3:
                    cogwheels[3] = rotate_counter_clockwise(cogwheels[3])
        elif num == 2 and dir == 1:
            cogwheels[1] = rotate_clockwise(cogwheels[1])
            if flag1:
                cogwheels[0] = rotate_counter_clockwise(cogwheels[0])
            if flag2:
                cogwheels[2] = rotate_counter_clockwise(cogwheels[2])
                if flag3:
                    cogwheels[3] = rotate_clockwise(cogwheels[3])
        elif num == 3 and dir == -1:
            cogwheels[2] = rotate_counter_clockwise(cogwheels[2])
            if flag3:
                cogwheels[3] = rotate_clockwise(cogwheels[3])
            if flag2:
                cogwheels[1] = rotate_clockwise(cogwheels[1])
                if flag1:
                    cogwheels[0] = rotate_counter_clockwise(cogwheels[0])
        elif num == 3 and dir == 1:
            cogwheels[2] = rotate_clockwise(cogwheels[2])
            if flag3:
                cogwheels[3] = rotate_counter_clockwise(cogwheels[3])
            if flag2:
                cogwheels[1] = rotate_counter_clockwise(cogwheels[1])
                if flag1:
                    cogwheels[0] = rotate_clockwise(cogwheels[0])
        elif num == 4 and dir == -1:
            cogwheels[3] = rotate_counter_clockwise(cogwheels[3])
            if flag3:
                cogwheels[2] = rotate_clockwise(cogwheels[2])
                if flag2:
                    cogwheels[1] = rotate_counter_clockwise(cogwheels[1])
                    if flag1:
                        cogwheels[0] = rotate_clockwise(cogwheels[0])
        elif num == 4 and dir == 1:
            cogwheels[3] = rotate_clockwise(cogwheels[3])
            if flag3:
                cogwheels[2] = rotate_counter_clockwise(cogwheels[2])
                if flag2:
                    cogwheels[1] = rotate_clockwise(cogwheels[1])
                    if flag1:
                        cogwheels[0] = rotate_counter_clockwise(cogwheels[0])
    print(calculate_point())


solution()
