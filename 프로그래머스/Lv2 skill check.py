from collections import defaultdict


def command_print(commands, dic):
    answer = []
    for i in range(len(commands)):
        command, user_id = commands[i]
        if command == "Enter":
            answer.append(dic[user_id] + "님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(dic[user_id] + "님이 나갔습니다.")
    return answer


def solution(record):
    dic = defaultdict()
    commands = []
    for i in range(len(record)):
        command = list(record[i].split())
        if command[0] == "Enter":
            dic[command[1]] = command[2]
            commands.append([command[0], command[1]])
        elif command[0] == "Leave":
            commands.append([command[0], command[1]])
        elif command[0] == "Change":
            dic[command[1]] = command[2]
    return command_print(commands, dic)


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
