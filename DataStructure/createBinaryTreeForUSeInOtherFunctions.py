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


a = [21,21,21,55,64,78,99,108,2828]

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
#printTree(t,"")


'''
CTCI question 4.10
Chceking whether a sub tree exists
'''
a1 = [1,2,3,4,4,6,7,8,9,10,11,12,13,14,15]
a2 = [1,2,3]
t1 = createBSTFromArray(a1,0,len(a1)-1)
t2 = createBSTFromArray(a2,0,len(a2)-1)
#printTree(t1,"")
#printTree(t2,"")
def checkSubTree(t1,t2):
    if not t1 or not t2:
        return False
    if t1.value == t2.value and validateSubTree(t1,t2):
        return True
    return checkSubTree(t1.left,t2)or checkSubTree(t1.right,t2)

def validateSubTree(t1,t2):
    if t1 == None and t2 == None:
        return True
    elif t1 == None or t2 == None:
        return False
    elif t1.value != t2.value :
        return False
    else:
        return validateSubTree(t1.left, t2.left) or validateSubTree(t1.right, t2.right)



#print(checkSubTree(t1,t2))




# To count paths with given sum:
def increaseDic(dict, key, delta):
    if not key in dict:
        dict[key] = 0
    dict[key] += delta


def countPaths(node, targetVal):
    if node == None:
        return 0
    pathCountDic = {}
    pathCountDic[0] = 1
    return countPathsInSubTree(node, targetVal, 0, pathCountDic)


def countPathsInSubTree(node, targetVal, runningSum, pathCountDic):
    if node == None:
        return 0
    runningSum += node.value
    increaseDic(pathCountDic, runningSum, 1)
    countToCount = runningSum - targetVal
    totalPaths = 0
    if countToCount in pathCountDic:
        totalPaths = pathCountDic[countToCount]

    totalPaths += countPathsInSubTree(node.left, targetVal, runningSum, pathCountDic)
    totalPaths += countPathsInSubTree(node.right, targetVal, runningSum, pathCountDic)
    increaseDic(pathCountDic, runningSum, -1)
    return totalPaths

print(printTree(t))
print(countPaths(t,42))