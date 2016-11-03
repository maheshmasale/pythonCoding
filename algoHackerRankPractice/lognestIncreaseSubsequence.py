sequence= [3, 45, 23,6,6, 9, 3, 99, 108, 76, 12, 77, 16, 18, 4]
#sequence = [2]
def findLongestIncreasingSubSequence(seqArr):
    if len(seqArr) < 2:
        return len(seqArr), len(seqArr), seqArr
    else:
        arrLongIncrSeq = list()
        arrLongIncrSeq.append([seqArr[0]])
        maxLen = 0
        l_arr = list()
        for i in range(1,len(seqArr)):
            previousMaxLength, previousMaxLengthIndex = 1,0
            for j in range(1,i):
                if seqArr[j] <= seqArr[i]:
                    if len(arrLongIncrSeq[j]) > previousMaxLength:
                        previousMaxLength = len(arrLongIncrSeq[j])
                        previousMaxLengthIndex = j
            tempArr = list(arrLongIncrSeq[previousMaxLengthIndex])
            tempArr.append(seqArr[i])
            arrLongIncrSeq.append(tempArr)
            l_arr.append(len(tempArr))
            if len(tempArr) > maxLen:
                maxLen = len(tempArr)

        return maxLen, l_arr, arrLongIncrSeq

print(findLongestIncreasingSubSequence(sequence))