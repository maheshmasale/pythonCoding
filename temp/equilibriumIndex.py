a = [5,4,2,6,8,3]

def findEquiInd(arr):
    if not arr or len(arr) < 1:
        return -1
    if len(arr) < 2:
        return 0
    i = 1
    j = len(arr) - 2
    lsum = arr[0]
    rsum =arr[-1]
    '''
    while(i<j):
        if lsum<rsum:
            lsum+=i
        i+=1
        j-=1
    '''
