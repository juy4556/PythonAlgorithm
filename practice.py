def solution(new_id):
    new_id = new_id.lower()  # stage1
    i = 0
    remove = []
    dot = []
    for n in range(len(new_id)):  # stage2
        if 'a' <= new_id[n] <= 'z':
            continue
        if 0 <= ord(new_id[n]) <= 9:
            continue
        if new_id[n] == '-' or new_id[n] == '_' or new_id[n] == '.':
            continue
        remove.append(n)
    for i in range(len(remove) - 1, -1, -1):
        new_id = new_id[:remove[i]] + new_id[remove[i] + 1:]
    index = 0
    while index < len(new_id):  # stage3
        index2 = index
        while new_id[index2] == '.':
            index2 += 1
        if index2 > index:
            dot.append([index, index2])
    dot.sort(key=lambda x: -x[0])
    for s, e in dot:
        new_id = new_id[:s + 1] + new_id[e:]
    new_id.strip('.')  # stage4
    if len(new_id) == 0:  # stage5
        new_id.append(a)
    if len(new_id) >= 16:  # stage6
        new_id = new_id[:16]
        if new_id[15] == '.':
            new_id = new_id[:15]
    if len(new_id) <= 2:  # stage7
        last = new_id[len(new_id) - 1]
        while len(new_id) <= 3:
            new_id = new_id + last

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
