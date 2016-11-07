#https://www.hackerrank.com/challenges/largest-rectangle
class stack():
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.arr)

    def pop(self):
        if self.size() > 0:
            return self.arr.pop()
        else:
            return None

    def push(self,val):
            self.arr.append(val)

    def peek(self):
        return self.arr[self.size() -1]


class editor():
    def __init__(self,string1):
        self.stringMain = string1
        self.commandList = stack()

    def isEmpty(self):
        return self.stringMain == ""

    def getLength(self):
        return len(self.stringMain)

    def append(self, strappend, avoidAppending = False):
        if self.isEmpty():
            self.stringMain = strappend
        else:
            self.stringMain += strappend
        if not avoidAppending:
            self.commandList.push([1,len(strappend)])

    def delete(self, k, avoidAppending = False):
        strDeleted = self.stringMain[self.getLength() - k:]
        self.stringMain = self.stringMain[:(self.getLength() -k)]
        if not avoidAppending:
            self.commandList.push([2, strDeleted])

    def print(self, k):
        if k <= self.getLength():
            print(self.stringMain[k-1])

    def undo(self):
        if not self.commandList.isEmpty() :
            self.commandArr = self.commandList.pop()
            if self.commandArr[0] == 1:
                self.delete(self.commandArr[1],True)
            else:
                self.append(self.commandArr[1],True)

strTemp = "MyNameIsMahesh"
editorObj = editor(strTemp)
editorObj.append(" ok")
print(editorObj.commandList.size())
print(editorObj.stringMain)
editorObj.delete(9)
print(editorObj.commandList.size())
print(editorObj.stringMain)
editorObj.undo()
print(editorObj.commandList.size())
print(editorObj.stringMain)
print(editorObj.commandList.size())
editorObj.undo()
print(editorObj.commandList.size())
print(editorObj.stringMain)