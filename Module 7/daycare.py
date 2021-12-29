

def minTrailerSpace(daycare, roomCap, trailerCap):

    # if daycare == []:
    #     return trailerCap

    for room in daycare:

        before = room[0]
        after = room[1]

        if trailerCap + roomCap < before:
            trailerCap += before - (trailerCap + roomCap)

        roomCap += after - before

    return trailerCap


def takeInput(daycares):
    try:

        while True:

            decreasing = []
            increasing = []
            same = []
            n = input()

            if ' ' not in n:
                n = int(n)

                for _ in range(n):
                    room = list(input().split())
                    room = [int(x) for x in room]

                    # increasing
                    if room[1] - room[0] > 0:
                        increasing.append(room)

                    # decreasing
                    elif room[1] - room[0] < 0:
                        decreasing.append(room)

                    # same
                    else:
                        same.append(room)

            daycares.append(increasing + same + decreasing)

    except:
        return


daycares = []
takeInput(daycares)

for daycare in daycares:

    rc = tc = 0
    def sorter(x): return (x[0]-x[1])
    daycare = sorted(daycare, key=sorter)
    # print(daycare)
    idx = 0
    for i in range(len(daycare) + 1):
        if i == len(daycare):
            break
        elif daycare[i][1] - daycare[i][0] <= 0:
            # idx = i
            break
    l1 = daycare[:i]
    l2 = daycare[i:]

    # all decreasing
    if l1 == []:
        l2 = sorted(l2, key=lambda x: (x[0], x[1]-x[0]), reverse=True)
        daycare = l2
    # all increasing
    elif l2 == []:
        l1 = sorted(l1, key=lambda x: (x[0], x[0]-x[1]))
        daycare = l1
    # both
    else:
        # print(l1)
        # print(l2)
        l1 = sorted(l1, key=lambda x: (x[0], x[0]-x[1]))
        l2 = sorted(l2, key=lambda x: (x[0], x[1]-x[0]), reverse=True)
        daycare = l1 + l2

    # print(daycare)
    print(minTrailerSpace(daycare, rc, tc))
