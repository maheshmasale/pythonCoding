import numpy as np

def tweetStrLen(arr,k):
    tempArr = []
    tempArr = np.cumsum(arr)


    maxLen = 0
    count = 0
    for j in range(len(arr)):
        for i in range(j, len(arr)):
            if j == 0:
                if tempArr[i] > k:
                    break
                if tempArr[i] <= k and (i-j+1) > count:
                    maxLen = tempArr[i]
                    count = i-j+1
            else:
                if tempArr[i] - tempArr[j-1] <= k and (i-j+1) > count:
                    maxLen = tempArr[i]- tempArr[j-1]
                    count = i - j+1
    return count
#print(tweetStrLen([1, 2, 3], 4))
print(tweetStrLen([3,1,2,1],4))
