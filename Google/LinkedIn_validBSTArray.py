def validateBSTArr(arr):
    min = None
    max = float('inf')
    if validateBSTArrRecur(arr,min,max,True):
        print("YES")
    else:
        print("NO")

def validateBSTArrRecur(arr,min,max,isLeftChild):
    if isLeftChild :
        if min != None and arr[0] >= min:
            return False

    #else:
    return True

arr = [3,2,1,5,4,6]

