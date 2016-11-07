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

arr = [5, 2, 3, 4, 3]

def largestRectangle(lst):
    maxArea = 0
    tp = 0
    i = 0
    s = stack()
    while i < len(lst):
        if s.isEmpty() or lst[s.peek()] < lst[i]:
            s.push(i)
            i += 1
        else:
            tp = s.pop()
            l_area = 0
            if s.isEmpty():
                l_area = lst[tp] * (i)
            else:
                l_area = lst[tp] * (i - s.peek()  - 1)
            #print(l_area)
            if maxArea < l_area:
                maxArea = l_area

    while not s.isEmpty():
        tp = s.pop()
        l_area = 0
        if s.isEmpty():
            l_area = lst[tp] * (i)
        else:
            l_area = lst[tp] * (i - s.peek() - 1)
        #print(l_area)
        if maxArea < l_area:
            maxArea = l_area

    return maxArea

print(largestRectangle(arr))