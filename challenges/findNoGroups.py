def findGroups(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                cnt += 1
                callDfsOnCell(arr,i,j)
    return cnt

def callDfsOnCell(arr,i,j):
    if arr[i][j] == 0:
        return
    arr[i][j] = 0
    if i > 0:
        callDfsOnCell(arr, i-1, j)
    if j > 0:
        callDfsOnCell(arr, i, j-1)

    if i<len(arr)-1:
        callDfsOnCell(arr, i + 1, j)
    if j<len(arr[0])-1:
        callDfsOnCell(arr, i, j + 1)

    '''
    #If diagonals are required.
    if i<len(arr)-1 and j > 0:
        callDfsOnCell(arr, i + 1, j-1)
    if i>0 and j > 0:
        callDfsOnCell(arr, i - 1, j-1)
    if i > 0 and j <len(arr[0])-1:
        callDfsOnCell(arr, i - 1, j + 1)
    if i < len(arr)-1 and j < len(arr[0]) - 1:
        callDfsOnCell(arr, i + 1, j + 1)
    '''

arr = [[0,0,0,1,0],[0,1,0,0,1],[1,1,1,0,0]]
print(findGroups(arr))


