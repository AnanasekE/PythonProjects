times = [['name1', 11, 12], ['name2', 10, 11], ['name5', 10, 12], ['name3', 15, 18], ['name4', 9, 18]]


def calc(day: list):
    i = 0
    plan = []
    lessonStart = 0

    day.sort(key=lambda x: (x[2], x[2] - x[1]))
    print(day)

    while i < len(times) - 1:
        if times[i][1] >= lessonStart:
            lessonStart = times[i][2]
            plan.append(times[i])
        i += 1
    return plan


print(calc(times))
