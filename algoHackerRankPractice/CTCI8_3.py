def getMagicNumberNoDuplicate(arr,start):
    #find mid
    mid = len(arr)//2
    print(mid,start,arr)
    if len(arr) == 0:
        return -1
    if arr[mid] == mid+start:
        return mid+start
    elif arr[mid] < mid+start:
    #search in mid+1 to endMid
        return getMagicNumberNoDuplicate(arr[mid+1:],mid+1)
    else:
    #search in arrayStart to mid+1
        return getMagicNumberNoDuplicate(arr[:mid],start)

def getMagicNumberWithDuplicate(arr,start):
    #find mid
    mid = len(arr)//2
    print(mid,start,arr)
    if len(arr) == 0:
        return False
    if arr[mid] == mid+start:
        return mid+start
    upperHalf, lowerHalf = False, False
    if mid+1 != len(arr):
        upperHalf = getMagicNumberWithDuplicate(arr[mid + 1:], mid + 1)
    if upperHalf:
        return upperHalf
    else:
        if mid != 0:
            lowerHalf = getMagicNumberWithDuplicate(arr[:mid], start)
        return lowerHalf

#print(getMagicNumberWithDuplicate([8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],0))
#print(getMagicNumberWithDuplicate([-1,1,1,5,8],0))


def  getAllPossibleSets(arrSet):
    tempSet = [[]]
    for i in range(len(arrSet)):
        tempSet.extend(getDoubleAddElem(tempSet,arrSet[i]))
    return tempSet

def getDoubleAddElem(mainSet,elem):
    from copy import deepcopy
    perc = deepcopy(mainSet)
    for i in range(len(perc)):
        perc[i].append(elem)
    return perc
print(getAllPossibleSets(['a','b','c']))