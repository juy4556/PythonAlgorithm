import sys
input = sys.stdin.readline

tc = int(input())
array = ['+', ' ', '-']

def solution(index):
    global formula
    global result
    if index > n:
        if result == 0:
            answer.append(formula)
        return

    for i in range(3):
        if i == 0:
            result += index
            formula += array[i]+str(index)
            solution(index+1)
            formula = formula[:-2]
            result -= index
        elif i == 1:
            formula += array[i]+str(index)
            temp = formula.replace(' ', '')
            result = eval(temp)
            solution(index + 1)
            formula = formula[:-2]
            temp = formula.replace(' ','')
            result = eval(temp)
        else:
            result -= index
            formula += array[i]+str(index)
            solution(index+1)
            formula = formula[:-2]
            result += index

for _ in range(tc):
    n = int(input())
    formula = '1'
    answer=[]
    result = 0
    solution(2)
    answer.sort()
    for i in answer:
        print(i)
    print()