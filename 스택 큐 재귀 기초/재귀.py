def recursive_function(i):
    if i == 5:
        return
    recursive_function(i+1)
    print('재귀 함수 호출')

recursive_function(0)

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지 차례대로 곱
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n*factorial_recursive(n-1)

print('반복적 구현:', factorial_iterative(5))
print('재귀적 구현:', factorial_recursive(5))