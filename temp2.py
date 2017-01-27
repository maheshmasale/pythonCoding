def getDuplicates(arr):
    from collections import Counter
    #return len([i for i, j in Counter(arr).items() if j > 1])
    return len(list(filter(lambda x: x[1] > 1, list(Counter(arr).items()))))

#print(getDuplicates([2, 3, 1, 1, 3]))

def isNumPowerOfFour(num):
    return num >0 \
           and bin(num).count('1')==1\
           and bin(num)[3:].count('0')%2==0
