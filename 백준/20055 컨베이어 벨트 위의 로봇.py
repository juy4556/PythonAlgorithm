from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
robot = deque()


def rotate_belt():
    global A
    A = [A.pop()] + A
    for i in range(len(robot)):
        robot[i] += 1
    if len(robot) > 0 and robot[0] >= N - 1:
        robot.popleft()


def move_robot():
    for i in range(len(robot)):
        next = robot[i] + 1
        if A[next] and next not in robot:
            A[next] -= 1
            robot[i] += 1
    if len(robot) > 0 and robot[0] >= N - 1:
        robot.popleft()


def push_robot():
    if A[0]:  # 내구도가 0이 아니라면
        robot.append(0)
        A[0] -= 1


def solution():
    count = 0
    while True:
        count += 1
        rotate_belt()
        move_robot()
        push_robot()
        if A.count(0) >= K:
            break
    print(count)


solution()
