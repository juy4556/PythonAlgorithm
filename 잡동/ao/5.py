def solution(n, tops):
    answer = 0
    length = 2 * n + 1
    dp = [0 for _ in range(length)]
    dp[0] = 1
    if tops[0] == 1:
        dp[1] = 3
    else:
        dp[1] = 2
    for i in range(2, length):
        if i & 1 and tops[i >> 1] & 1:
            dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 10007
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    answer = dp[-1]
    return answer


print(solution(4, [1, 1, 0, 1]))  # 149
print(solution(2, [0, 1]))  # 11
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # 7704
