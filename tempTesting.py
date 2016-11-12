def weave(lArr,rArr, prefix,permuArr = []):
    #use recursion to find the permutations of given sequence by keeping the sequence intact.
    if len(lArr) ==0 and len(rArr) == 0:
        permuArr.append(prefix)
        return permuArr
    if len(lArr) == 0:
        tempPrefix = []
        tempPrefix.extend(prefix)
        tempPrefix.extend(rArr)
        permuArr.append(tempPrefix)
        return permuArr
    if len(rArr) == 0:
        tempPrefix = []
        tempPrefix.extend(prefix)
        tempPrefix.extend(lArr)
        permuArr.append(tempPrefix)
        return permuArr

    lArrTemp = lArr[1:]
    rArrTemp = rArr[1:]

    tempPrefix = []
    tempPrefix.extend(prefix)

    tempPrefix.append(lArr[0])
    weave(lArrTemp,rArr,tempPrefix,permuArr)
    tempPrefix.pop()
    tempPrefix.append(rArr[0])
    weave(lArr,rArrTemp, tempPrefix ,permuArr)
    tempPrefix.pop()
    return permuArr

permutationsArr = weave(["a","b","c"],["d","e","f"],"",[])
print(permutationsArr)