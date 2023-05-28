def solution(book_time):
    hours = []
    rooms = []
    for i in range(len(book_time)):
        start_hour, start_min = map(int, book_time[i][0].split(":"))
        end_hour, end_min = map(int, book_time[i][1].split(":"))
        hours.append([start_hour, start_min, end_hour, end_min])

    hours = sorted(hours, key=lambda x: (x[0], x[1]))
    rooms.append([hours[0]])
    for i in range(1, len(hours)):
        sh, sm, eh, em = hours[i]
        flag = False
        for j in range(len(rooms)):
            if 60 * sh + sm >= 60 * rooms[j][-1][2] + rooms[j][-1][3] + 10:
                rooms[j].append(hours[i])
                flag = True
        if not flag:
            rooms.append([hours[i]])
    print(len(rooms))
    print(rooms)
    return len(rooms)


solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])
solution([["09:10", "10:10"], ["10:20", "12:20"]])
solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])
