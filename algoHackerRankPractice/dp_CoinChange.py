#Dynamic program to get minimum change of the given number!
#denomination = [50,25,10,5,1]



#Dynamic programming - bottom up approach
denomination = [10,6,1]
def makeChange(amt):
    arrChng = [i for i in range(amt+1)]
    print(arrChng)
    for i in range(1,amt+1):
        q = i
        j = 0
        while q < denomination[j]:
            j+=1
        #print(denomination[j])
        divi = q // denomination[j]
        for itr in range(divi+1):
            print(i,denomination[j],itr,q,arrChng  )
            if itr == 0:
                if j+1 < len(denomination):
                    q = min(q, 1 + arrChng[i - denomination[j+1]])
            else:
                q = min(q,itr+arrChng[i - itr*denomination[j]])
            #print(q)
        arrChng[i] = q
        #print(i, arrChng[i])
    return arrChng[amt]

print(makeChange(12))

'''
denomination = [10,6,1]
#Dynamic programming with Memoizing
minChange = {}
def makeChange(amt,i):
    if amt in minChange:
        return minChange[amt]
    if amt == 0:
        return 0
    if amt == denomination[i]:
        return 1
    elif amt < denomination[i]:
        if i+1 < len(denomination):
            return makeChange(amt,i+1)
        else:
            return amt
    else:
        divi = amt//denomination[i]
        count = amt
        for j in range(divi,-1,-1):
            if i+1 < len(denomination):
                countAhead = makeChange(amt - denomination[i] * j,i+1)
            else:
                continue
            if countAhead+j < count:
                count = countAhead+j
        if amt in minChange:
            if minChange[amt] > count:
                minChange[amt] = count
        else:
            minChange[amt] = count
        return count

'''