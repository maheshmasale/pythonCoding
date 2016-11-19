def validateBSTArr(arr):
    minRng = -float('inf')
    if validateBSTArrRecur(arr,minRng):
        print("YES")
    else:
        print("NO")

def validateBSTArrRecur(arr,minRng):
    if len(arr) == 0:
        return True
    if arr[0] <= minRng:
        return False
    indexR = getIndexForRightArr(arr)
    #print(arr, indexR,minRng)
    return validateBSTArrRecur(arr[1:indexR],minRng) and (validateBSTArrRecur(arr[indexR:],arr[0]) if indexR != len(arr) else True)

def getIndexForRightArr(arr):
    nodeVal = arr[0]
    i = 1
    while i < len(arr) and nodeVal > arr[i]:
        i += 1
    return i

arr = [3,2,1,5,4,6]
#arr = [1,3,4,2]
validateBSTArr(arr)