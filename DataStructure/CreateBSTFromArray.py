from collections import deque
from itertools import permutations

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


def getSize(t, counter):
    if t == None:
        return counter
    else:
        counter = counter + 1
        counter = getSize(t.left, counter)
        counter = getSize(t.right, counter)
    return counter

t = createBSTFromArray(a,0,len(a)-1)
printTree(t,"")
print(getSize(t,0))


def findAllTopologySequences(rootNode):
    que = deque()
    que.append(rootNode)
    arrSeque = []
    while len(que) > 0:
        tempArr = []
        for i in range(len(que)):
            a = que.pop()
            tempArr.append(a.left)
            tempArr.append(a.right)
            
            if len(arrSeque) == 0:
                arrSeque.append(a.val)
            else:
