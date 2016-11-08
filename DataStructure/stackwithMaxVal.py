class stack():
    def __init__(self):
        self.arr = []
        self.maxValArr = []

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.arr)

    def pop(self):
        if self.size() > 0:
            self.maxValArr.pop()
            return self.arr.pop()
        else:
            return None

    def push(self,val):
        if self.size() == 0:
            self.arr.append(val)
            self.maxValArr.append(val)
        else:
            maxVal = self.maxValArr[self.size()-1]
            self.arr.append(val)
            if val > maxVal:
                self.maxValArr.append(val)
            else:
                self.maxValArr.append(maxVal)

    def maxVal(self):
        return self.maxValArr[self.size() -1]


s = stack()
s.push(12)
s.push(32)
s.push(2)
print(s.maxVal())
print(s.pop())
print(s.arr)
