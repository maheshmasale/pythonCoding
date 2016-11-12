def weave(lArr,rArr, prefix = [],permuArr = []):

    #use recursion to find the permutations of given sequence by keeping the sequence intact.
    if len(lArr) ==0 and len(rArr) == 0:
        permuArr.append(prefix)
        return permuArr
    if len(lArr) == 0:
        permuArr.append(prefix.extend(rArr))
        return permuArr
    if len(rArr) == 0:
        permuArr.append(prefix.extend(lArr))
        return permuArr

    lArrTemp = lArr[1:]
    rArrTemp = rArr[1:]
    print(prefix)
    weave(lArrTemp,rArr,prefix.append(str(lArr[0])),permuArr)
    weave(lArr,rArrTemp,prefix.append(str(rArr[0])),permuArr)
    return permuArr

permutationsArr = weave(["a","b","c"],["d","e","f"],[],[])
print(permutationsArr)