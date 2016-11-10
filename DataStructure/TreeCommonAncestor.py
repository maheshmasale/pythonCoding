class Node():
    def __init__(self,val):
        if val == Node:
            raise ValueError
        self.value = val
        self.left = None
        self.right = None
        self.parent = None


a = [21,55,64,78,99,108,2828]

def createBSTFromArray(a,start,end):
    if start > end:
        return None
    else:
        mid = int((start+end)/2)
        n = Node(a[mid])
        t = createBSTFromArray(a,start,mid-1)
        n.left = t
        if t:
            t.parent = n
        x = createBSTFromArray(a,mid+1,end)
        n.right = x
        if x:
            x.parent = n
        return n

def printTree(t,str):
    if t == None:
        return
    print(str,t.value)
    str = str + "    "
    if t.left != None:
        printTree(t.left,str)

    if t.right != None:
        printTree(t.right,str)


t = createBSTFromArray(a,0,len(a)-1)
printTree(t,"")

def findCommonAncestor(nodeA, nodeB):
    #find path of nodeA and put it stackA
    stackA = []
    while(nodeA.parent):
        stackA.append(nodeA.parent)
        nodeA = nodeA.parent
    #find path of nodeB and put it stackB
    stackB = []
    while(nodeB.parent):
        stackB.append(nodeB.parent)
        nodeB = nodeB.parent

    #pop from StackA and StackB and compare
    while len(stackA) > 0 and len(stackB) > 0:
        topElem = stackA[-1]
        if stackA.pop() != stackB.pop():
            return topElem.parent

    return None

print(t.left.left.value, t.right.right.value)
print(findCommonAncestor(t.left.left,t.right.right).value)