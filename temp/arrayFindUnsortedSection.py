def getArrSectToSort(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i] <= arr[i+1]:
            i += 1
        else:
            break
    left = i
    if left == len(arr)-2:
        return 0
    i = len(arr)-1
    while i > 1:
        if arr[i] >= arr[i-1]:
            i -= 1
        else:
            break
    right = i

    maxInd = left
    minInd = right
    for j in range(left+1,right):
        if arr[j] > arr[maxInd]:
            maxInd = j
        if arr[j] < arr[minInd]:
            minInd = j

    while(right<len(arr) and arr[maxInd] > arr[right]):
        right+=1
    while(left > -1 and arr[minInd] < arr[left]):
        left-=1
    return (left+1,right-1)


def getPrevIndex(arr,i,j,flg):
    if j == -1:
        j = i
    if flg:
        while(j >=0):
            if arr[j] > arr[i+1]:
                j-=1
            else:
                break
        return j
    else:
        while (j < len(arr)):
            if arr[j] < arr[i]:
                j += 1
            else:
                break
        return j

def getArrSectToSortDiffMethod(arr):
    j = -1
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            j = getPrevIndex(arr, i,j,True)
    k = -1
    for i in range(len(arr)-1,0,-1):
        if arr[i] < arr[i - 1]:
            k = getPrevIndex(arr, i, k, False)
    return (j+1 if j>-1 else 0,k if k < len(arr) else len(arr)-1)

arr = [1,2,4,7,10,11,7,12,6,7,16,18,19]
arr = [1,2,6,5,5,8,9]
#arr = [8,7,6,5,4,3,2,1]
#1st Method
sect = getArrSectToSort(arr)
print(sect)
#second method
sect = getArrSectToSortDiffMethod(arr)
print(sect)
print(sect[1]-sect[0]+1)




