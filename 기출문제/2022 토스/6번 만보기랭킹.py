steps_one, steps_two, steps_three = [], [], []
names_one, names_two, names_three = [], [], []
N, M, P = map(int, input().split())
for _ in range(N):
    step, name = input().split()
    steps_one.append(int(step))
    names_one.append(name)
for _ in range(M):
    step, name = input().split()
    steps_two.append(int(step))
    names_two.append(name)
for _ in range(P):
    step, name = input().split()
    steps_three.append(int(step))
    names_three.append(name)


def sol(names, steps, num):
    temp = set()
    arr = []
    for i in range(num):
        if names[i] not in temp:
            temp.add(names[i])
            arr.append([names[i], steps[i]])
        else:
            for j in range(len(arr)):
                if arr[j][0] == names[i]:
                    arr[j][1] = max(arr[j][1], steps[i])
    return arr


def solution():
    one, two, three = [], [], []
    result = []
    a = set()
    one = sol(names_one, steps_one, N)
    two = sol(names_two, steps_two, M)
    three = sol(names_three, steps_three, P)
    arr = one + two + three

    for i in range(len(one) + len(two) + len(three)):
        if arr[i][0] not in a:
            a.add(arr[i][0])
            result.append(arr[i])
        else:
            for j in range(len(result)):
                if result[j][0] == arr[i][0]:
                    result[j][1] += arr[i][1]
    result.sort(key=lambda x: (-x[1], x[0]))
    ans = []
    for i in range(len(result)):
        ans.append(result[i][0])
    print(ans)


solution()
