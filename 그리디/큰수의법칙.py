n, m, k = map(int, input("n,m,k 입력:").split()) # input()은 입력 값을 문자열로 인식
data = list(map(int, input("n개의 자연수 입력:").split()))
result = 0

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째 큰 수

count = (m / (k+1)) * k
count += m % (k+1)

result = 0
result += count*first
result += (m-count)*second

print(result)