'''
다익스트라 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 특정 노드에서 출발해 다른 노드로 가는 각각의 최단경로를 구해주는 알고리즘이다.
이 알고리즘은 음의 간선이 없을 때 정상 작동하고, 실제 GPS 소프트웨어의 기본 알고리즘으로 사용된다.
다익스트라 알고리즘은 기본적으로 그리디 알고리즘으로 분류된다.(매번 가장 비용이 적은 노드를 선택해서 임의의 과정 반복하기 때문)
과정은 다음과 같다.
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산하여 최단 거리 테이블 갱신
5. 3, 4번 반복
단계마다 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 순차 탐색한다.
해당 알고리즘은 O(V^2), 이 때 V는 노드 수
'''
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한값 10억으로 설정

n, m = map(int, input().split()) # n은 node 수, m은 간선 수
start = int(input()) # 시작 노드 번호 입력
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드까지 가는 비용이 c
    graph[a].append((b, c))

# 가장 최단 거리가 짧은 노드의 인덱스 찾기
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        print(j[0])
        print(j[1])
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i], end=' ')