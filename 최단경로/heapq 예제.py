'''
파이썬 내장 라이브러리 heapq는 최소힙구조
'''
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 힙 h에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result1 = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result1)


'''
최대힙 구현방법
'''

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 힙 h에 삽입
    for value in iterable:
        heapq.heappush(h, -value) # 부호를 임시로 변경
    # 힙에 삽입된 모든 원소를 차례로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h)) # 힙에서 원소를 꺼낼 때 부호를 다시 변경하여 최대힙 구현
    return result

result2 = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result2)
