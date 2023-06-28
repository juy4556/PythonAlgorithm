import sys

input = sys.stdin.readline


def bellman_ford(start):
    dist = [int(1e9) for _ in range(N + 1)]
    dist[start] = 0
    for n in range(N):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if n == N - 1:  # 마지막 N-1번째에도 dist를 감소하는 것은 음수 사이클 존재한다는 뜻
                    return True

    return False


if __name__ == "__main__":
    TC = int(input())
    for _ in range(TC):
        N, M, W = map(int, input().split())
        edges = []
        for _ in range(M):
            S, E, T = map(int, input().split())
            edges.append((S, E, T))
            edges.append((E, S, T))

        for _ in range(W):
            S, E, T = map(int, input().split())
            edges.append((S, E, -T))

        if bellman_ford(1):
            print("YES")
            continue
        print("NO")
