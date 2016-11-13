
def weave(lArr,rArr, prefix,permuArr = []):
    #use recursion to find the permutations of given sequence by keeping the sequence intact.
    tempPrefix = []
    tempPrefix.extend(prefix)
    if len(lArr) ==0 or len(rArr) == 0:
        tempPrefix.extend(lArr)
        tempPrefix.extend(rArr)
        permuArr.append(tempPrefix)
        return permuArr

    tempPrefix.append(lArr[0])
    weave(lArr[1:],rArr,tempPrefix,permuArr)
    tempPrefix.pop()
    tempPrefix.append(rArr[0])
    weave(lArr,rArr[1:], tempPrefix ,permuArr)
    tempPrefix.pop()
    return permuArr

#permutationsArr = weave(["a","b","c"],["d","e","f"],"",[])
permutationsArr = weave(["a","b"],["d","e"],"",[])
print(permutationsArr)
