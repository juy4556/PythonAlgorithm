from itertools import combinations, product
from collections import defaultdict


def calculate_comb_sums(dice, comb):
    sum_count = defaultdict(int)
    for outcome in product(*[dice[i] for i in comb]):
        sum_count[sum(outcome)] += 1
    return sum_count


def compare_comb(comb1_sums, comb2_sums):
    wins, draws, losses = 0, 0, 0

    for sum1, count1 in comb1_sums.items():
        for sum2, count2 in comb2_sums.items():
            if sum1 > sum2:
                wins += count1 * count2
            elif sum1 == sum2:
                draws += count1 * count2
            else:
                losses += count1 * count2

    return wins, draws, losses


def solution(dice):
    n = len(dice)
    answer = []
    result_comb = []
    max_win_rate = 0

    summaries = {comb: calculate_comb_sums(dice, comb)
                 for comb in combinations(range(n), n // 2)}

    compare_count = 0
    for comb in combinations(range(n), n // 2):
        if compare_count == n // 2 + 1:
            break
        opposite_comb = tuple(set(range(n)) - set(comb))
        # print(comb, opposite_comb)
        wins, draws, losses = compare_comb(summaries[comb], summaries[opposite_comb])

        total_games = wins + draws + losses
        win_rate = 0
        losses_rate = 0
        if total_games > 0:
            win_rate = wins / total_games
            losses_rate = losses / total_games

        if win_rate > max_win_rate:
            max_win_rate = win_rate
            result_comb = comb

        if losses_rate > max_win_rate:
            max_win_rate = losses_rate
            result_comb = opposite_comb
        compare_count += 1

    answer = [i + 1 for i in result_comb]
    return answer


# [1, 4]
print(solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))
# [2]
print(solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]))
# [1, 3]
print(solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]))
