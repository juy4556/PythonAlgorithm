if __name__ == "__main__":
    S = list(' '.join(list(input().rstrip())).split())
    T = list(' '.join(list(input().rstrip())).split())
    result = 1
    while T:
        if T[-1] == 'A':
            T.pop()
        elif T[-1] == 'B':
            T.pop()
            T.reverse()

        if len(T) == len(S):
            for i in range(len(T)):
                if T[i] != S[i]:
                    result = 0
            break

    print(result)