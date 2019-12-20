class Node:
    def __init__(self, name):
        self.name = name
        self.prev = None
    
    def setPrevNode(self, other):
        self.prev = other


def Day6(filename):
    lines = open(filename, 'r').read().splitlines()

    nodeList = []

    for data in lines:
        names = data.split(")")
        exists = False

        for item in nodeList:
            if item.name == names[0]:
                exists = True
                node1 = item

        if not exists:
            node1 = Node(names[0])
            nodeList.append(node1)

        node2 = Node(names[1])
        node2.setPrevNode(node1)
        nodeList.append(node2)

    totalOrbits = 0

    for item in nodeList:
        while item.prev != None:  
            totalOrbits += 1
            item = item.prev
    return totalOrbits

print(Day6("data.txt"))