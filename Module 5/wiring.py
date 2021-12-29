

class FindUnion:
    def __init__(self, arr = []) -> None:
        self.arr = arr

    def find(self, node):

        for i, each in enumerate(self.arr):
            if each[0] == node:
                index = i

        while self.arr[index][-1] != index:
            index = self.arr[index][-1]
            index = self.find(self.arr[index][0])

        return self.arr[index][-1]


    def union(self, node1, node2):

        i1 = self.find(node1)
        i2 = self.find(node2)

        if self.arr[i1][-1] != self.arr[i2][-1]:
            self.arr[i1][-1] = self.arr[i2][-1]




def kruskals(fu, wires):

    cost = 0
    for wire in wires:
        t1 = fu.find(wire.node1.name)
        t2 = fu.find(wire.node2.name)


        if t1 != t2:
            cost += wire.cost 
            fu.union(wire.node1.name, wire.node2.name)
            # print("addedtotree", wire.node1.name, wire.node2.name, wire.cost)

    return cost


class House:

    def __init__(self):
        self.nodes = {}
        self.wires = []


class Node:

    def __init__(self, name, type):
        self.name = name
        self.type = type 
        self.neighbors = []
        self.neighborLights = []
        self.lights = set()
        self.parent = None


class Wire:

    def __init__(self, node1, node2, cost):
        self.node1 = node1
        self.node2 = node2
        self.cost = cost


def takeInput(n, w, house, fu, switches):

    recentSwitch = None
    for i in range(n):
        node, type = input().split()
        newNode = Node(node, type)
        if newNode.type == 'switch':
            recentSwitch = newNode
            switches.append(newNode)
        elif newNode.type == 'light':
            recentSwitch.lights.add(node)
            newNode.parent = recentSwitch
        house.nodes[node] = newNode
        fu.arr.append([newNode.name, i])
        # TODO add node to find union structure

    for _ in range(w):
        
        n1, n2, cost = input().split()
        cost = int(cost)

        node1 = house.nodes[n1]
        node2 = house.nodes[n2]

        if node1.type in {'outlet', 'box', 'breaker'} and node2.type in {'outlet', 'box', 'breaker'}:
            house.wires.append(Wire(node1, node2, cost))

        elif node1.type == 'switch' and node2.type == 'light':
            if node2.name in node1.lights:
                node1.neighborLights.append(Wire(node1, node2, cost))


        elif node1.type == 'light' and node2.type == 'switch':
            if node1.name in node2.lights:
                node2.neighborLights.append(Wire(node1, node2, cost))

        elif node1.type == 'switch' and node2.type in {'outlet', 'breaker', 'box'}:
            node1.neighbors.append(Wire(node1, node2, cost))

        elif node2.type == 'switch' and node1.type in {'outlet', 'breaker', 'box'}:
            node2.neighbors.append(Wire(node1, node2, cost))

        elif node1.type == 'light' and node2.type == 'light':
            if node1.parent == node2.parent:
                node1.parent.neighborLights.append(Wire(node1, node2, cost))



# N = number of nodes
# W = number of possible wires
N, W = input().split()
N, W = int(N), int(W)

House = House()
FU = FindUnion()
switches = []
# print('--------')
c = takeInput(N, W, House, FU, switches)

House.wires.sort(key=lambda x: x.cost)


totalCost = 0
for node in switches:
    if node.type == 'switch':
        # print(node.name)
        fu = FindUnion()
        node.neighborLights.sort(key=lambda x: x.cost)
        node.neighbors.sort(key=lambda x: x.cost)
        totalCost += kruskals(fu, node.neighborLights)
        totalCost += node.neighbors[0].cost


# print('----------')
print(kruskals(FU, House.wires) + totalCost)

