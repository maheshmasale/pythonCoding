
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


'''
We have adjacency list
{ "a" : [b,c],"b" : [c],"c" : [d]"d" : []}
'''


def createGraphAutomate(m,k):
    g = Graph()
    tempArr = []
    for i in range(1,m+1):
        i = Node(i)
        tempArr.append(i)
    for j in range(1,m):
        ndElm = max(1, j // k)
        if not tempArr[ndElm-1] in tempArr[j].getAdjacents():
            tempArr[j].addAdjacents(tempArr[ndElm-1])
        if not tempArr[j] in tempArr[ndElm - 1].getAdjacents():
            tempArr[ndElm-1].addAdjacents(tempArr[j])
    for i in range(m):
        g.addVertices(tempArr[i])
    printGraph(g)

createGraphAutomate(15,2)
