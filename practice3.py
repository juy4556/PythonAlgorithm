def solution(s):
    count = 0
    opens = {'(', '[', '{'}
    closes = {')', ']', '}'}
    small = {'(', ')'}
    mid = {'{', '}'}
    large = {'[', ']'}
    open_close_mapping = {'(': ')', '[': ']', '{': '}', ')': '(', ']': '[', '}': '{'}
    length = len(s)
    lack = find_lack(s)
    opposite = open_close_mapping[lack]
    lack_type = {lack, opposite}
    other_type = {}
    another_type = {}
    lack_stack = []
    other_stack = []
    another_stack = []
    if lack_type == small:
        other_type = mid
        another_type = large
    elif lack_type == mid:
        other_type = small
        another_type = large
    else:
        other_type = small
        another_type = mid

    stack = []
    right_count = 0
    right = []
    last_index = 0
    if lack in opens:
        for i in range(length):
            if s[i] in opens:
                if s[i] in lack_type:
                    stack.append(0)
                    lack_stack.append(i)
                elif s[i] in other_type:
                    stack.append(1)
                    other_stack.append(i)
                else:
                    stack.append(2)
                    another_stack.append(i)

            else:
                if s[i] in lack_type:
                    if stack and stack[-1] != 0:
                        last_index = i
                        break

                    if lack_stack:
                        lack_stack.pop()
                    else:
                        last_index = i
                        break

                elif s[i] in other_type:
                    if stack and stack[-1] == 1:
                        stack.pop()
                    if other_stack:
                        a = other_stack.pop()
                        b = i
                        right.append((a, b))

                else:
                    if stack and stack[-1] == 2:
                        stack.pop()
                    if another_stack:
                        a = another_stack.pop()
                        b = i
                        right.append((a, b))
        other = 0
        another = 0
        if other_stack:
            other = other_stack[-1]
        if another_stack:
            another = another_stack[-1]
        start_index = max(other, another)
        print("start, last: ", start_index, last_index)
        while start_index <= last_index:
            for i in range(len(right)):
                if start_index == right[i][0]:
                    start_index = right[i][1] + 1
                    continue
            if s[start_index] in lack_type:
                count += 1
            start_index += 1
        count += len(right)

    else:
        for i in range(length - 1, -1, -1):
            if s[i] in closes:
                if s[i] in lack_type:
                    stack.append(0)
                    lack_stack.append(i)
                elif s[i] in other_type:
                    stack.append(1)
                    other_stack.append(i)
                else:
                    stack.append(2)
                    another_stack.append(i)

            else:
                if s[i] in lack_type:
                    if stack and stack[-1] != 0:
                        last_index = i
                        break

                    if lack_stack:
                        lack_stack.pop()
                    else:
                        last_index = i
                        break

                elif s[i] in other_type:
                    if stack and stack[-1] == 1:
                        stack.pop()
                    if other_stack:
                        a = other_stack.pop()
                        b = i
                        right.append((b, a))

                else:
                    if stack and stack[-1] == 2:
                        stack.pop()
                    if another_stack:
                        a = another_stack.pop()
                        b = i
                        right.append((b, a))
        other = length
        another = length
        if other_stack:
            other = other_stack[-1]
        if another_stack:
            another = another_stack[-1]
        start_index = min(other, another) - 1
        print("start, last: ", start_index, last_index)
        right.sort()
        while last_index <= start_index:
            flag = 0
            for i in range(len(right)):
                if last_index == right[i][0]:
                    last_index = right[i][1] + 1
                    right_count += 1
                    flag = 1
                    break
            if flag:
                continue
            if s[last_index] in lack_type:
                count += 1
            last_index += 1
        print(count, right_count)
        count += right_count

    print(lack)
    print(stack)
    print("last_idx: ", last_index)
    print("right: ", right)
    print("lack_stack: ", lack_stack)
    print("other: ", other_stack)
    print("another: ", another_stack)

    return count


def find_lack(s):
    bracket_count = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}

    for c in s:
        bracket_count[c] += 1

    if bracket_count['('] < bracket_count[')']:
        return '('
    elif bracket_count['('] > bracket_count[')']:
        return ')'
    elif bracket_count['['] < bracket_count[']']:
        return '['
    elif bracket_count['['] > bracket_count[']']:
        return ']'
    elif bracket_count['{'] < bracket_count['}']:
        return '{'
    elif bracket_count['{'] > bracket_count['}']:
        return '}'
    else:
        raise ValueError("Invalid bracket string")


if __name__ == "__main__":
    print(solution("[]([[]){}"))  # 3, ]
    print(solution("{([()]))}"))  # 4, (
    print(solution("(()()()"))  # 7, )
    print(solution("{(([)]))}"))  # 1, (
    print(solution("{[[{}()[]]}"))  # 7, ]
    print(solution("["))
    # start = time.time()
    # ss = "".join("(" for _ in range(250000)) + "".join((')' for _ in range(249999)))
    # print(ss)
    # start = time.time()
    # print(solution(ss))
    # end = time.time()
    # print(end - start)
