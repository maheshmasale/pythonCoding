
class Graph():
    def __init__(self):
        self.countVertices = 0
        self.vertices = []

    def addVertices(self, vertice):
        self.vertices.append(vertice)
        self.countVertices += 1

    def getVetices(self):
        return self.vertices

class Node():
    def __init__(self, vertex):
        self.visited = False
        self.adjacencyList = []
        self.vertex = vertex

    def addAdjacents(self, adjacent):
        if adjacent != None:
            self.adjacencyList.append(adjacent)

    def getAdjacents(self):
        return self.adjacencyList

    def getVertex(self):
        return self.vertex


def createGraph():
    g = Graph()

    x = Node("x")
    y = Node("y")
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    x.addAdjacents(y)
    x.addAdjacents(a)
    a.addAdjacents(y)
    b.addAdjacents(c)
    c.addAdjacents(d)
    d.addAdjacents(x)
    y.addAdjacents(a)

    g.addVertices(x)
    g.addVertices(y)
    g.addVertices(a)
    g.addVertices(b)
    g.addVertices(c)
    g.addVertices(d)

    return g

def breadthFirstSearch(g, start,end):
    if start == end:
        return True

    que = []
    que.append(start)

    while len(que) > 0:
        t = que[0]
        t.visited = True
        adjacentsList = t.getAdjacents()
        for i in range(len(adjacentsList)):
            temp = adjacentsList[i]
            que = que[1:]
            if not temp.visited:
                temp.visited = True
                if temp == end:
                    return True
                que.append(temp)
    return False

def printGraph(g):
    v = g.vertices
    for i in v:
        print(i.vertex , " --->", end = " ")
        for j in i.getAdjacents():
            print(j.getVertex(), end = " ")
        print()

graphhh =  createGraph()
printGraph(graphhh)
print(breadthFirstSearch(graphhh, graphhh.getVetices()[4] , graphhh.getVetices()[1]))