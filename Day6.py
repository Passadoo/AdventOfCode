class Node:
    def __init__(self, name):
        self.name = name
        self.prev = None
    
    def setPrevNode(self, other):
        self.prev = other


def Day6(filename):
    with open(filename) as f:
        lines = f.readlines()
    
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

        if names[1] not in nodeList:
            node2 = Node(names[1])
            node2.setPrevNode(node1)
            nodeList.append(node2)

    totalOrbits = 0

    for item in nodeList:
        if item.name == "K":
            example = item
    
    iteration = 0
    while example.prev is not None:
        print("iteration nr " + str(iteration))
        print("Name: " + str(example.name))
        example = example.prev

    for item in nodeList:
        oldTotal = totalOrbits
        print("Adding orbits for " + str(item.name))
        while item.prev != None:  
            totalOrbits += 1
            item = item.prev
        nrOrbitsAdded = totalOrbits - oldTotal
        print(str(nrOrbitsAdded) + " orbits added")
    return totalOrbits

print(Day6("data.txt"))