
import time

'''
brute force closest pair of points
'''


def bruteForce(case):
    closest = float('inf')
    for p1 in case:
        for p2 in case:
            if p1 != p2:
                d = calculateDistance(p1, p2)
                if d < closest:
                    closest = d
    return closest


'''
utility function to calculate the distance between two points
'''


def calculateDistance(tup1, tup2):
    return (((tup2[0] - tup1[0])**2) + ((tup2[1] - tup1[1])**2))**0.5


'''
recursive helper function
'''


def divideAndConquerHelper(sortedByX):

    # if number of points is small, use bruteForce()
    if len(sortedByX) <= 3:
        return bruteForce(sortedByX)

    # find the middle point in the sortedByX array
    mid = len(sortedByX) // 2
    # store the point at mid in variable midpoint for later
    midPoint = sortedByX[mid]

    # recursively calculate the smallest distance on the left and right of mid
    smallestDistanceOnLeft = divideAndConquerHelper(sortedByX[:mid])
    smallestDistanceOnRight = divideAndConquerHelper(sortedByX[mid:])

    # d is used to calclate which points should be in the runway
    d = min(smallestDistanceOnLeft, smallestDistanceOnRight)

    runway = []

    # loop through points sorted by x,
    # if within d of midPoint's x value, add to runway
    for point in sortedByX:
        if abs(point[0] - midPoint[0]) < d:
            runway.append(point)

    # sort the runway by y
    runway.sort(key=lambda y: y[1])

    # initialize the smallest distance in the runway to d
    smallestInRunway = d

    # loop through the points in the runway
    for i in range(len(runway)):
        j = i + 1
        # loop through the next 7 points in runway
        # calculate the distance between the current point and the next 7
        while j < len(runway) and j - i <= 8:
            distance = calculateDistance(runway[i], runway[j])

            # if the distance is smaller than smallestInRunway, update smallestInRunway
            if distance < smallestInRunway:
                smallestInRunway = distance

            j += 1

    # return the smallest of smallestDistanceOnLeft, smallestInRunway, smallestDistanceOnRight
    return min(smallestDistanceOnLeft, min(smallestInRunway, smallestDistanceOnRight))


'''
divide and conquer closest pair of points
'''


def divideAndConquer(case):
    case.sort(key=lambda x: x[0])
    sortedByX = case
    smallestDistance = divideAndConquerHelper(sortedByX)
    if smallestDistance > 10000:
        return 'infinity'
    else:
        return "{:.4f}".format(smallestDistance)


'''
recursive function to read input and store in cases
'''


def takeInput(n, cases):
    case = []
    for _ in range(n):
        x, y = input().split()
        case.append((float(x), float(y)))

    cases.append(case)

    n = input()
    n = int(n)

    if n != 0:
        takeInput(n, cases)


'''
driver code
'''
cases = []
n = input()
n = int(n)

takeInput(n, cases)

# counter = 1
for case in cases:
    # bruteStart = time.perf_counter_ns()
    # print(bruteForce(case))
    # bruteEnd = time.perf_counter_ns()
    # print(f"Brute Force runtime for case{counter}: {(bruteEnd - bruteStart)/1000000}")
    # DCStart = time.perf_counter_ns()
    print(divideAndConquer(case))
    # DCEnd = time.perf_counter_ns()
    # print(f"D&C runtime for case{counter}: {(DCEnd - DCStart)/1000000}")
    # counter += 1


"""
References:

https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-by-second-item/

    - tup.sort(key = lambda x: x[1]) 

https://pynative.com/python-input-function-get-user-input/

    - input(), input().split()

"""
