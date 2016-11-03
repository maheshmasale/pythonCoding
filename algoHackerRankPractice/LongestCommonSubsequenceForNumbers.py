#seq = [3, 45, 23,6,6, 9, 3, 99, 108, 76, 12, 77, 16, 18, 4]

def findLongestIncreasingSubSequence(seqArr):
    seqArrSorted = sorted(seqArr)

    lengthSeq = len(seqArr)
    c = [list(0 for i in range(lengthSeq)) for j in range(lengthSeq)]
    b = [list(0 for i in range(lengthSeq)) for j in range(lengthSeq)]

    for i in range(lengthSeq):
        for j in range(lengthSeq):
            if seqArr[i] == seqArrSorted[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 2
            elif c[i-1][j] >= c[i][j-1]:
                c[i][ j] = c[i - 1][ j ]
                b[i][ j] = 1
            else:
                c[i][ j] = c[i ][ j- 1]
                b[i][ j] = 0

    i = lengthSeq -1
    j = lengthSeq-1
    lcsStr = list()
    while(i >=0 and j >= 0):
        if b[i][j] == 2:
            lcsStr.append(seqArr[i])
            i=i-1
            j=j-1
        elif b[i][j] == 1:
            i=i-1
        else:
            j=j-1
    lcsStr.reverse()
    return lcsStr

print(findLongestIncreasingSubSequence(seq))