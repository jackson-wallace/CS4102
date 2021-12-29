

'''
An optimal set of registrations may cause an individual student to be enrolled in too few or too many
classes. The algorithm must ensure that this does not happen (although that may not be possible,
given the constraints). For simplicity’s sake, we’ll just have a number n which is the exact number
of courses each student must be enrolled in: no more, no less.

Each course has a course cap which is the maximum number of students that can enroll in the course.

r is the number of student registration requests, 
c is the number of courses, and 
n is the number of classes each student is to be enrolled in


For each course, c is the weight of the edge from the course to the sink

for each student, n is the weight of the edge from s to the student

for each request, there is an edge of weight one from the student to the class
'''


class Graph:

    def __init__(self, studentDict, courseDict, n) -> None:

        self.idxDict = {}

        for i, student in enumerate(studentDict, start=1):
            self.idxDict[student] = i
        for j, course in enumerate(courseDict, start=i+1):
            self.idxDict[course] = j

        self.size = len(studentDict) + len(courseDict) + 2

        self.G = [[0 for i in range(self.size)] for j in range(self.size)]

        for student in studentDict:
            self.G[0][self.idxDict[student]] = int(n)

            for request in studentDict[student]:
                self.G[self.idxDict[student]][self.idxDict[request]] = 1

        for course in courseDict:
            self.G[self.idxDict[course]][self.size - 1] = courseDict[course]

    def DFS(self, s, t, path):

        visited = [False for _ in range(self.size)]

        stack = []

        stack = [0]
        visited[s] = True

        while stack:
            # print(stack)

            u = stack.pop(0)

            for i, val in enumerate(self.G[u]):
                if visited[i] == False and val > 0:

                    stack.append(i)
                    visited[i] = True
                    path[i] = u
                    if i == t:
                        return True
        # print(path)
        return False

    def fordFulkerson(self):
        source = 0
        sink = len(self.G) - 1

        path = [-1 for _ in range(self.size)]
        maxFlow = 0

        while self.DFS(source, sink, path):

            minFlow = float("Inf")
            s = sink
            while(s != source):
                # print(path_flow)
                minFlow = min(minFlow, self.G[path[s]][s])
                s = path[s]

            maxFlow += minFlow

            i = sink
            while(i != source):
                j = path[i]
                self.G[j][i] -= minFlow
                self.G[i][j] += minFlow
                i = path[i]
        # print(self.G)
        # print(max_flow)
        return maxFlow


def readInput(allStudents, allCourses, ns):

    while True:

        r, c, n = input().split()
        r, c, n = int(r), int(c), int(n)

        if r == 0 and c == 0 and n == 0:
            break

        students = {}
        courses = {}
        ns.append(n)

        for _ in range(r):

            student, course = input().split()

            if student in students:
                students[student].append(course)
            else:
                students[student] = [course]

        for _ in range(c):

            course, capacity = input().split()
            course = course

            courses[course] = int(capacity)

        allStudents.append(students)
        allCourses.append(courses)

        x = input()


allStudents = []
allCourses = []
ns = []

readInput(allStudents, allCourses, ns)

# print(allStudents)
# print(allCourses)


for i in range(len(allStudents)):

    # print(allStudents[i], allCourses[i])
    if allStudents[i] == {}:
        print('Yes')
    else:
        g = Graph(allStudents[i], allCourses[i], ns[i])
        # for row in g.G:
        #     print(row)
        flow = g.fordFulkerson()

        if flow < ns[i] * len(allStudents[i]):
            print('No')
        else:
            print('Yes')
