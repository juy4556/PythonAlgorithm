import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    numbers = input().rstrip()
    length = len(numbers)
    stack = [numbers[0]]
    index = 1
    while index < length:
        while K and stack and numbers[index] > stack[-1]:
            stack.pop()
            K -= 1
        stack.append(numbers[index])
        index += 1
    if K:
        stack = stack[:-K]
    print("".join(stack))
