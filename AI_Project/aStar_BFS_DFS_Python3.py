import re
from math import *

try:
    import Queue as queue
except ImportError:
    import queue as queue

class Graph():
    def __init__(self):
        self.countVertices = 0
        self.cityList = []

    def addCity(self, cityMem):
        self.cityList.append(cityMem)
        self.countVertices += 1

    def getCities(self):
        return self.cityList

    def getCity(self,cityName):
        for i in self.cityList:
            if i.cityName == cityName:
                return i

    def printGraph(self):
        print("PRINTING GRAPH:")
        for i in self.cityList:
            print(i.getName(), " --->", end=" ")
            for j in i.getAdjacents():
                print(j[0].getName(),'(',j[1],')', end=" ")
            print()
        return "END OF Graph"

    def resetGraph(self):
        for i in self.getCities():
            i.visited = False
            i.distFromSrc = float('inf')
            i.estimatedDistToTrgt = float('inf')
            i.prevCityInPath = None

class city():
    def __init__(self, cityName,longitude,lat,distFromSrcParam=float('inf'),estimatedDistToTrgtParam=float('inf')):
        self.visited = False
        self.adjacencyList = []
        self.cityName = cityName
        self.latitude = lat
        self.longitude = longitude
        self.distFromSrc = distFromSrcParam
        self.estimatedDistToTrgt = estimatedDistToTrgtParam
        self.prevCityInPath = None

    def addAdjacents(self, adjacent):
        if adjacent:
            self.adjacencyList.append(adjacent)

    def getAdjacents(self):
        return self.adjacencyList

    def getName(self):
        return self.cityName

    def getDistance(self,otherCity):
        R = 6371
        # return ((self.longitude - otherCity.longitude)**2 + (self.latitude - otherCity.latitude)**2)**0.5
        dlon = (self.longitude - otherCity.longitude) * pi / 180
        dlat = (self.latitude - otherCity.latitude) * pi / 180
        a = (sin(dlat / 2)) ** 2 + cos(self.latitude * pi / 180) * cos(otherCity.latitude * pi / 180) * ((sin(dlon / 2)) ** 2)
        c = 2 * atan2(a**0.5, (1 - a)**0.5)
        return R*c

    def getExtractedPath(self,otherCity):
        path = []
        currCity = self
        while currCity != None and currCity.getName() != otherCity.getName():
            path.append(currCity.getName())
            currCity = currCity.prevCityInPath
        path.append(otherCity.getName())
        return path[::-1]

    #for Ver <3.0
    def __cmp__(self, other):
        return self.estimatedDistToTrgt < other.estimatedDistToTrgt
    #for Ver >3.0
    def __lt__(self, other):
        return self.estimatedDistToTrgt < other.estimatedDistToTrgt

class searchGraph():

    def createGraph(self,roads, cities):
        g = Graph()
        for k, v in cities.items():
            x = city(k, v['long'], v['lat'])
            g.addCity(x)
        for i in roads:
            city1 = g.getCity(i[0])
            city2 = g.getCity(i[1])
            city1.addAdjacents((city2, i[2]))
            city2.addAdjacents((city1, i[2]))
        return g

    def readPrologFile(self,filename):
        '''
        :param filename: This is the name of the prolog file to be read.
        :return: This function should return a tuple of roads array and a dictionary of city details .
        '''

        outData = ''
        roads = []
        cityLoc = {}

        with open(filename, 'r', encoding='utf-8') as f:
            outData = f.read()

        allRoads = re.findall(r'(?<=road).*,.*,.*[)](?=.)', outData)
        allCities = re.findall(r'(?<=city).*,.*,.*[)](?=.)', outData)

        for i in allRoads:
            i = i[1:-1].split(',')
            try:
                roads.append([str.strip(i[0]), str.strip(i[1]), int(str.strip(i[2]))])
            except:
                pass
        for i in allCities:
            i = i[1:-1].split(',')
            try:
                cityLoc[i[0].strip()] = {'lat': float(i[1].strip()), 'long': float(i[2].strip())}
            except:
                pass
        return (roads, cityLoc)

    def __init__(self,fileName):
        tupRoadCities = self.readPrologFile(fileName)    #'./roads.pl')
        self.graph = self.createGraph(tupRoadCities[0],tupRoadCities[1])

    def __repr__(self):
        return self.graph.printGraph()

    def breadthFirstSearch(self, start, end):
        if start == end:
            return [],[]

        startCity = self.graph.getCity(start)
        endCity = self.graph.getCity(end)

        path = []
        que = []
        que.append(startCity)
        while len(que) > 0:
            t = que[0]
            t.visited = True
            path.append(t.getName())
            adjacentCities = t.getAdjacents()
            for i in range(len(adjacentCities)):
                tempCity = adjacentCities[i][0]
                if not tempCity.visited:
                    #For getting the path
                    tempCity.prevCityInPath = t

                    tempCity.visited = True
                    if tempCity.getName() == endCity.getName():
                        return path,endCity.getExtractedPath(startCity)
                    que.append(tempCity)
            que = que[1:]
        return [],endCity.getExtractedPath(startCity)

    def depthFirstSearch(self, start, end):
        if start == end:
            return [],[]

        startCity = self.graph.getCity(start)
        endCity = self.graph.getCity(end)

        path = []
        stk = []

        stk.append(startCity)
        while len(stk) > 0:
            tempCity = stk.pop()
            path.append(tempCity.getName())
            tempCity.visited = True
            adjacentCities = tempCity.getAdjacents()

            for i in range(len(adjacentCities)):
                tCity = adjacentCities[i][0]
                if not tCity.visited:

                    #For getting the path
                    tCity.prevCityInPath = tempCity

                    tCity.visited = True
                    if tCity.getName() == endCity.getName():
                        return path, tCity.getExtractedPath(startCity)
                    stk.append(tCity)
        return [],endCity.getExtractedPath(startCity)

    def calcHeuristicDist(self,targetCity):
        dictHDist = {}
        for iCity in self.graph.getCities():
            dictHDist[iCity.getName()] = targetCity.getDistance(iCity)
        return dictHDist

    def AStarSearch(self,start,end):
        if start == end:
            return [],[]
        startCity = self.graph.getCity(start)
        endCity = self.graph.getCity(end)

        HeurDistDict = self.calcHeuristicDist(endCity)
        setattr(startCity,'distFromSrc',0)
        print("The Heuristic Distance Values are")
        for k,v in HeurDistDict.items():
            print(k,"=",v)
        print(" ")

        path = []
        que = queue.PriorityQueue()
        que.put(startCity)
        while not que.empty():
            currCity = que.get()
            #print('Start Of the City----------------------',currCity.getName())
            path.append(currCity.getName())
            for adjCityTup in currCity.getAdjacents():
                tempCity = adjCityTup[0]
                if tempCity.getName() == end:
                    setattr(tempCity,'prevCityInPath' ,currCity)
                    return path, endCity.getExtractedPath(startCity)

                g = getattr(currCity,'distFromSrc',0)+adjCityTup[1]
                h = HeurDistDict[tempCity.getName()]
                if g < getattr(tempCity,'distFromSrc',0):
                    setattr(tempCity,'distFromSrc',g)
                    setattr(tempCity,'estimatedDistToTrgt',g+h)
                    setattr(tempCity,'prevCityInPath' ,currCity)
                    que.put(tempCity)
                #print('------------', tempCity.getName(), tempCity.distFromSrc,tempCity.estimatedDistToTrgt)
            #print('End Of the City----------------------')
        return [], endCity.getExtractedPath(startCity)

def question1(fileName):
    print('Start of Question 1')
    print('Path is between Urziceni and Mehadia')
    test1 = searchGraph(fileName)
    bfsArr,bfsPath = test1.breadthFirstSearch('urziceni','mehadia')
    test1.graph.resetGraph()
    dfsArr,dfsPath = test1.depthFirstSearch('urziceni','mehadia')
    print("BFS opened",len(bfsArr),"number of nodes.")
    print("DFS opened",len(dfsArr),"number of nodes.")
    print("BFS visited following cities :",",".join(bfsArr))
    print("DFS visited following cities :",",".join(dfsArr))

    print("BFS Path :"," -> ".join(bfsPath))
    print("DFS Path :"," -> ".join(dfsPath))
    
    print('End of Question 1','\n')

def question2(fileName):
    print('Start of Question 2')
    print('Path is between Arad and Lugoj')
    test1 = searchGraph(fileName)
    bfsArr,bfsPath = test1.breadthFirstSearch('arad', 'lugoj')
    test1.graph.resetGraph()
    dfsArr,dfsPath = test1.depthFirstSearch('arad', 'lugoj')
    print("BFS opened", len(bfsArr), "number of nodes.")
    print("DFS opened", len(dfsArr), "number of nodes.")
    print("BFS visited following cities :", ",".join(bfsArr))
    print("DFS visited following cities :", ",".join(dfsArr))

    print("BFS Path :"," -> ".join(bfsPath))
    print("DFS Path :"," -> ".join(dfsPath))
    
    print('End of Question 2','\n')

def question3(fileName):
    print('Start of Question 3')
    print('Path is between Arad and Neamt')
    test1 = searchGraph(fileName)
    #test1.graph.printGraph()
    dfsArr,dfsPath = test1.depthFirstSearch('arad', 'neamt')

    test1.graph.resetGraph()
    aStarArr,aStarPath = test1.AStarSearch('arad', 'neamt')

    print("DFS opened", len(dfsArr), "number of nodes.")
    print("A Star opened", len(aStarArr), "number of nodes.")
    print("DFS visited following cities :", ",".join(dfsArr))
    print("A Star visited following cities :", ",".join(aStarArr))

    print("DFS Path :"," -> ".join(dfsPath))
    print("A* Path :"," -> ".join(aStarPath))

    print('End of Question 3','\n')

question1('./roads.pl')
question2('./roads.pl')
question3('./roads.pl')