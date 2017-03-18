def getLongestTwoCharStr(str1):
    if len(str1) <= 2:
        return str1
    dictChr = {}
    dictChr[str1[0]] = 1
    i,j = 0,1
    outputStr = ""
    while j < len(str1):
        if str1[j] in dictChr:
            dictChr[str1[j]] += 1
        else:
            if len(dictChr) > 1:
                if len(outputStr) < (j-i):
                    outputStr = str1[i:j]
                preChr = str1[j-1]
                tempArr = dictChr.keys()
                for k in tempArr:
                    if k!= preChr:
                        #dictChr.pop(k,None)
                        removeKey = k
                dictChr.pop(removeKey, None)
                i = j-1
                while str1[i] == preChr and i > -1:
                    i -=1
                i += 1
            dictChr[str1[j]] = 1
        j += 1

    if len(outputStr) < (j - i):
        outputStr = str1[i:j]
    return outputStr



str1 = "aababaacacaccccadefab"
print(getLongestTwoCharStr(str1))