def findSumTwoArrays(arr1,arr2,tot):
    #return true if sum found
    #arr1Dict = dict(zip(arr1,range(len(arr1))))
    return len([i for i in arr2 if (tot-i) in set(arr1)])

print(findSumTwoArrays([5,7,2,4],[-3,0,1],9))