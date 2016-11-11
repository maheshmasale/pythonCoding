class Node():
    def __init__(self,val):
        if val == None:
            raise ValueError
        self.value = val
        self.left = None
        self.right = None


def getZigZagTreeOutPut(r):
    s = list()
    s.append()
    s.append(r)
    flag = True
    outputArr = []
    while len(s)>0:
        tempStack = []
        for i in s:
            temp = s.pop()
            if flag:
                if temp.left:
                    tempStack.append(temp.left)
                if temp.right:
                    tempStack.append(temp.right)
            else:
                if temp.right:
                    tempStack.append(temp.right)
                if temp.left:
                    tempStack.append(temp.left)
            flag = not flag

        s = tempStack
        outputArr = outputArr[0:] + tempStack[0:]
