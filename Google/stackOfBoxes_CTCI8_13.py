def createStacks(boxArr):
    boxArr = sorted(boxArr,reverse = True)
    maxHeight = 0
    for i in range(len(boxArr)):
        height = createStack(boxArr,i)
        maxHeight = max(maxHeight,height)

    return maxHeight

def createStack(boxArr,ind):
    baseHeight = boxArr[ind].height
    maxHeight = 0
    i = ind+1
    while i < len(boxArr):
        #print(i,len(boxArr))
        if boxArr[ind].canBeAbove(boxArr[i]):
            height = createStack(boxArr,i)
            maxHeight = max(maxHeight,height)
        i = i +1
    return maxHeight+baseHeight

class Boxes():
    def __init__(self,x,y,z):
        if not x or not y or not z:
            return None
        self.height = x
        self.width = y
        self.depth = z

    def __lt__(self, other):
        return self.height < other.height

    def canBeAbove(self,other):
        return other.width <= self.width and other.depth <= self.depth

a = Boxes(1,1,1)
b = Boxes(7,8,8)
c = Boxes(3,12,3)
d = Boxes(4,8,6)
e = Boxes(5,8,6)
f = Boxes(6,4,6)
arr = [a,b,c,d,e,f]

print(createStacks(arr))