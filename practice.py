def solution(histroy, option, keyword):
    answer = []
    # if len(option) == 0:
    #     for h in hisotry
    for i in range(len(option)):
        option_name, flag = option[i][0], option[i][1]
        if flag == "F":
            answer.append("empty")
            continue
        for h in histroy:
            str = list(h.split(" "))
            if keyword in str:
                answer.append(h)

    if len(answer) < 1:
        answer.append("empty")
    answer = list(set(answer))
    return answer


if __name__ == "__main__":
    history = ["hello i am david", "hello kail", "hi tina"]
    option = [["W", "T"]]
    keyword = "hello"

    print(solution(history, option, keyword))
