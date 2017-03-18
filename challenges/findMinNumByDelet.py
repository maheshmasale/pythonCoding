def findMinNumyDelet(numStr,delCnt):
    return getMostLowNum(numStr,len(numStr)-delCnt) if len(numStr) >= delCnt else 0
def getMostLowNum(numStr,numCnt):
    if numCnt == len(numStr):
        return numStr
    ind = numStr.find(min([i for i in numStr[:(len(numStr)-numCnt+1)]]))
    return str(numStr[ind]) + getMostLowNum(numStr[ind+1:],numCnt-1)


print(findMinNumyDelet('43597658',2))