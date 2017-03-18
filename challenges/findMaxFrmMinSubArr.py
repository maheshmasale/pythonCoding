def getMaxOfMinSubarr(arr,x):
    j = 0
    maxVal = -float('inf')
    while j< len(arr)-x:
        minVal = min(arr[j:j+x])
        if minVal > maxVal:
            maxVal = minVal
        j+=1
    return maxVal
#print(getMaxOfMinSubarr([2,5,4,6,8],3))

def getTotalSwaps(arr):
    j = 0
    startVal = arr[0]
    cnt = 0
    while j < len(arr):
        if arr[j] == startVal:
            j+=1
        if arr[j] != startVal:
            break
    zeroCnt = 0
    while j< len(arr):
        if arr[j] == 0:
            zeroCnt += 1
        else:
            if zeroCnt > 0:
                cnt = 2*cnt + zeroCnt
                zeroCnt = 0
        j+=1

    return cnt

print(getTotalSwaps([1,0,0,0,0,1,1,0]))
#print(getTotalSwaps([1,1,1,0,1,0,1]))