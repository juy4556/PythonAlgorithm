def computeLPS(pattern, lps):
    start = 0  # length of the previous LPS(Longest proper prefix which is suffix)

    # 항상 lps[0]==0이므로 while문은 i는 1부터 시작한다.
    end = 1
    while end < len(pattern):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if pattern[start] == pattern[end]:
            start += 1
            lps[end] = start
            end += 1
        else:
            # 일치하지 않는 경우
            if start != 0:
                # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
                start = lps[start - 1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                lps[end] = 0
                end += 1


def KMPSearch(txt, pattern):
    i = 0  # index for txt[]
    j = 0  # index for pattern[]
    while i < N:
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
        if pattern[j] == txt[i]:
            i += 1
            j += 1
        # pattern을 찾지 못한 경우
        elif pattern[j] != txt[i]:
            # j!=0인 경우는 짧은 lps에 대해 재검사
            if j != 0:
                j = lps[j - 1]
            # j==0이면 일치하는 부분이 없으므로 인덱스 증가
            else:
                i += 1

        # pattern을 찾은 경우
        if j == M:
            print(1)
            return
    print(0)
    return


if __name__ == "__main__":
    txt = input()
    pattern = input()
    M = len(pattern)
    N = len(txt)
    lps = [0] * M
    # Preprocess the pattern
    computeLPS(pattern, lps)
    KMPSearch(txt, pattern)
