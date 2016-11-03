x1,v1,x2,v2 = 23, 9867, 9814, 5861
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]n = int(input())
s = set(map(int, input().split()))
operationsList = []
m = int(input())

for i in range(m):
    operationsList.append(input().strip().split())

for i in range(m)
    {
        "pop" : lambda a : a.pop(),
        "discard" : lambda  a,x: a.discard(x),
        "remove" : lambda  a,x: a.remove(x)
    }[operationsList[i][0]]()

print(sum(s))