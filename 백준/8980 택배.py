import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N, C = map(int, input().split())
    M = int(input())
    villeges = []
    for _ in range(M):
        send, receive, box = map(int, input().split())
        villeges.append((send - 1, receive - 1, box))

    villeges.sort(key=lambda x: (x[1], x[0]))
    upper_bound = [C for _ in range(N + 1)]
    result = 0
    for i in range(M):
        send, receive, box = villeges[i]
        min_box = C
        for j in range(send, receive):
            min_box = min(min_box, upper_bound[j])
        min_box = min(min_box, box)
        for j in range(send, receive):
            upper_bound[j] -= min_box
        result += min_box
    print(result)
