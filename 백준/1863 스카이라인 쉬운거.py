import sys

input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    stack = []
    height_set = set()
    count = 0
    buildings = []
    for _ in range(n):
        x, y = map(int, input().split())
        buildings.append((x, y))

    buildings.sort(key=lambda x: x[0])

    for i in range(n):
        x, y = buildings[i]
        while stack and stack[-1] > y:
            height_set.remove(stack.pop())
            count += 1
        if y > 0 and y not in height_set or stack and stack[-1] < y:
            stack.append(y)
            height_set.add(y)

    count += len(stack)

    print(count)
