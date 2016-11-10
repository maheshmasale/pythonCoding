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

l_dict = {")":"(","]":"[","}":"{"}

s = "]"
def bracketMatching(str):
    s = stack()
    for i in str:
        if s.size() == 0:
            s.push(i)
            #print(i, s.peek())
        else:
            #print(i, s.arr,s.peek())
            if i in l_dict.keys() and s.peek() == l_dict[i]:
                s.pop()
            else:
                s.push(i)
    return s.size() == 0

if bracketMatching(s):
    print("YES")
else:
    print("NO")