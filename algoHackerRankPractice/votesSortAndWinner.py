from operator import itemgetter

v = ["l", "r", "l", "l","r"]

countV = []
setV = set(v)
for i in setV:
    countV.append(v.count(i))

zipped = zip(setV,countV)
arr = sorted(zipped, key=itemgetter(1,0),  reverse=True )

print(arr[0][0])




