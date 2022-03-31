n = int(input())

num = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_result = -(1e9)
min_result = 1e9

def dfs(result,index,plus, minus, mul, div):
    global max_result
    global min_result
    if index == n:
        max_result = max(max_result,result)
        min_result = min(min_result,result)
        return
    if plus > 0:
        dfs(result + num[index], index+1,plus-1,minus,mul,div)
    if minus > 0:
        dfs(result - num[index], index+1,plus,minus-1,mul,div)
    if mul > 0:
        dfs(result * num[index], index+1,plus,minus,mul-1,div)
    if div > 0:
        if result<0:
            dfs((abs(result)//num[index])*(-1), index + 1, plus, minus, mul, div - 1)
        else:
            dfs(result//num[index], index + 1, plus, minus, mul, div-1)

dfs(num[0],1, plus, minus, mul, div)

print(max_result)
print(min_result)