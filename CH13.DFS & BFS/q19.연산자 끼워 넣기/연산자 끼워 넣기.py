import sys

input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
min_result = 1e9
max_result = -(1e9)

result = l[0]


def calculation(result, index, plus, minus, mul, div):
    global min_result, max_result
    if index == n:
        if min_result > result:
            min_result = result
        if max_result < result:
            max_result = result
    else:
        if plus > 0:
            plus -= 1
            calculation(result + l[index], index + 1, plus, minus, mul, div)
            plus += 1
        if minus > 0:
            minus -= 1
            calculation(result - l[index], index + 1, plus, minus, mul, div)
            minus += 1
        if mul > 0:
            mul -= 1
            calculation(result * l[index], index + 1, plus, minus, mul, div)
            mul += 1
        if div > 0:
            div -= 1
            if result < 0:
                calculation(-1*(-1*result//l[index]),index + 1, plus, minus, mul, div)
            else:
                calculation(result // l[index], index + 1, plus, minus, mul, div)
            div += 1


calculation(result, 1, plus, minus, mul, div)

print(max_result)
print(min_result)
