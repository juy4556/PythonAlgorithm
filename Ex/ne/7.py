#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximizeTransactions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY transaction as parameter.
#

def maximizeTransactions(transaction):
    dp = [[0, 0] for _ in range(len(transaction))]
    answer = 0
    idx = 0
    while idx < len(transaction) and transaction[idx] < 0:
        dp[idx] = [transaction[idx], 0]
        idx += 1
    if idx < len(transaction):
        dp[idx] = [transaction[idx], 1]

    for i in range(idx + 1, len(transaction)):
        dp[i][0] = transaction[i]
        for j in range(i - 1, -1, -1):
            if dp[j][0] >= 0 and dp[i][0] + dp[j][0] >= 0:
                if dp[i][0] <= transaction[i] + dp[j][0] and dp[i][1] <= dp[j][1] + 1:
                    dp[i][0] = transaction[i] + dp[j][0]
                    dp[i][1] = dp[j][1] + 1
        answer = max(answer, dp[i][1])
    print(dp)
    return answer


'''
13
-1
3
2
-5
-3
-1
-2
-2
4
-2
-1
-3
-1
'''

if __name__ == '__main__':
    transaction_count = int(input().strip())

    transaction = []

    for _ in range(transaction_count):
        transaction_item = int(input().strip())
        transaction.append(transaction_item)

    result = maximizeTransactions(transaction)

    print(result)
