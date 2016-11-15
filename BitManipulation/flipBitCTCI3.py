def flipBit(num):
    binStr = bin(num)[2:]
    maxLen, preCnt, cnt = 0,0,0
    for i in range(len(binStr)):
        if int(binStr[i]) == 1:
            cnt += 1
        elif i > 0 and int(binStr[i-1]) == 0:
                preCnt = 0
        else:
            if cnt+preCnt+1 > maxLen:
                maxLen = cnt+preCnt+1
            preCnt = cnt
            cnt = 0

    if cnt + preCnt+1 > maxLen:
        maxLen = cnt + preCnt + 1

    if maxLen > len(binStr):
        maxLen = len(binStr)


    return maxLen

print(flipBit(1))