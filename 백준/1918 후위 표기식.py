if __name__ == "__main__":
    equation = input()
    stack = []
    result = ""
    for s in equation:
        if 'A' <= s <= 'Z':
            result += s
        else:
            if s == '(':
                stack.append(s)
            elif s == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
            elif s == '*' or s == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    result += stack.pop()
                stack.append(s)
            elif s == '+' or s == '-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(s)
    while stack:
        result += stack.pop()
    print(result)
