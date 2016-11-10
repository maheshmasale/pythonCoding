class Node():
    def __init__(self,val):
        if val == Node:
            raise ValueError
        self.value = val
        self.left = None
        self.right = None


a = [21,55,64,78,99,108,2828]
def createBSTFromArray(a,start,end):
    if start > end:
        return None
    else:
        mid = int((start+end)/2)
        n = Node(a[mid])
        n.left = createBSTFromArray(a,start,mid-1)
        n.right = createBSTFromArray(a,mid+1,end)
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

