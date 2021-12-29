
def longestPath(grid):

    pathDict = {}
    elevations = []

    cols = len(grid)
    rows = len(grid[0])
    for i in range(cols):            # i is y-axis
        for j in range(rows):        # j is x-axis
            pathDict[(i, j)] = 1     # initialize all paths to 1
            elevations.append([grid[i][j], i, j])

    elevations.sort(key=lambda x: x[0], reverse=True)

    for point in elevations:
        curr = point[0]
        i = point[1]
        j = point[2]
        # up
        if i-1 >= 0 and grid[i-1][j] < curr:
            pathDict[(i-1, j)] = pathDict[(i, j)] + 1 if pathDict[(i, j)
                                                                  ] + 1 > pathDict[(i-1, j)] else pathDict[(i-1, j)]

        # down
        if i+1 < cols and grid[i+1][j] < curr:
            pathDict[(i+1, j)] = pathDict[(i, j)] + 1 if pathDict[(i, j)
                                                                  ] + 1 > pathDict[(i+1, j)] else pathDict[(i+1, j)]

        # left
        if j-1 >= 0 and grid[i][j-1] < curr:
            pathDict[(i, j-1)] = pathDict[(i, j)] + 1 if pathDict[(i, j)
                                                                  ] + 1 > pathDict[(i, j-1)] else pathDict[(i, j-1)]

        # left
        if j+1 < rows and grid[i][j+1] < curr:
            pathDict[(i, j+1)] = pathDict[(i, j)] + 1 if pathDict[(i, j)
                                                                  ] + 1 > pathDict[(i, j+1)] else pathDict[(i, j+1)]

    return max(list(pathDict.values()))


def readInput(numCities, grids, cities):
    try:
        for _ in range(numCities):
            l = list(input().split())

            city, rows, cols = l[0], int(l[1]), int(l[2])

            cities.append(city + ': ')

            grid = []

            for _ in range(cols):

                row = list(input().split())
                row = [int(x) for x in row]

                grid.append(row)

            grids.append(grid)
    except:
        return


numCities = int(input())
grids = []
cities = []

readInput(numCities, grids, cities)

for i, grid in enumerate(grids):
    print(cities[i] + str(longestPath(grid)))
