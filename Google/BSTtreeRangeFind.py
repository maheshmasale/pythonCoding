class Node():
    def __init__(self,val):
        if val == Node:
            raise ValueError
        self.x = val
        self.l = None
        self.r = None


a = [21,55,64,78,99,108,2828]

def createBSTFromArray(a,start,end):
    if start > end:
        return None
    else:
        mid = int((start+end)/2)
        n = Node(a[mid])
        t = createBSTFromArray(a,start,mid-1)
        n.l = t
        x = createBSTFromArray(a,mid+1,end)
        n.r = x
        return n

def printTree(t,str):
    if t == None:
        return
    print(str,t.x)
    str = str + "    "
    if t.l != None:
        printTree(t.l,str)

    if t.r != None:
        printTree(t.r,str)


t = createBSTFromArray(a,0,len(a)-1)
printTree(t,"")
#=================================================================================================







































# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, T):
    # write your code in Python 2.7
    if T == None:
        return 0

    counter = getMinMaxOFGivenTree(T, None, None, A, B)
    return counter


def getSize(t, size):
    if t == None:
        return size
    else:
        size = size + 1
        size = getSize(t.l, size)
        size = getSize(t.r, size)
    return size


def getMinMaxOFGivenTree(T, min, max, A, B):
    if T == None:
        return 0
    if min == None:
        leftMinFind = T
        while (leftMinFind.l):
            leftMinFind = leftMinFind.l
        min = leftMinFind.x
    if max == None:
        rightMaxFind = T
        while (rightMaxFind.r):
            rightMaxFind = rightMaxFind.r
        max = rightMaxFind.x

    if min > A and max < B:
        return getSize(T, 0)
    else:
        counter = None
        counter1 = None

        if T.l:
            counter = getMinMaxOFGivenTree(T.l, min, T.x, A, B)
        if T.r:
            counter1 = getMinMaxOFGivenTree(T.r, T.x, max, A, B)

        if not counter and not counter1:
            return 0
        elif not counter and counter1:
            return counter1
        elif not counter1 and counter:
            return counter
        else:
            if counter > counter1:
                return counter
            else:
                return counter1


print(solution(5,79,t))