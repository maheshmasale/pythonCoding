def checkSequenceViolation(arrLocks):
    stk = []
    DictTemp = {}

    for i in range(len(arrLocks)):
        num = arrLocks[i].split(' ')[1]
        if arrLocks[i][0] == "A":
            if num in DictTemp and DictTemp[num] == True:
                return i+1
            stk.append(num)
            DictTemp[num] = True
        else:
            if num not in DictTemp or DictTemp[num] == False:
                return i+1
            if stk[-1] != num:
                return i+1
            stk.pop()
            DictTemp[num] = False
    if len(stk) > 0:
        return len(arrLocks) + 1
    return 0

print(checkSequenceViolation(["ACQUIRE 123","ACQUIRE 122", "ACQUIRE 85", "RELEASE 85","RELEASE 122","RELEASE 123","ACQUIRE 145"]))