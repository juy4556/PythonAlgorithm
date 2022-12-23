def func(x):
    if not x:
        return
    else:
        return int(x)


t = int(input())  # 테스트 케이스 개수(최대 100)

for i in range(t):
    flag = 0
    p = input()  # 수행할 함수 p(1이상 100,000이하)
    n = int(input())  # 배열에 들어있는 수의 개수 n

    array = list(map(func, input().strip("[]").split(",")))
    reverse_count = 0

    if n == 0:
        array = []
    for j in p:
        if j == 'R':
            reverse_count += 1
        elif j == 'D':
            if not array:
                flag = 1
                print("error")
                break
            else:
                if reverse_count % 2 == 0:
                    del array[0]
                else:
                    del array[len(array) - 1]

    if reverse_count % 2 == 1:
        array.reverse()

    if flag == 0:
        print(array)
