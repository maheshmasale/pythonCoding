from unittest.mock import _patch


def findPathExist(mat):
    path = []
    allPaths = []
    cachePath = {}
    return checkPath(mat,(0,0), (len(mat)-1,len(mat[0])-1),path,allPaths,cachePath)



def checkPath(mat,start, end,path,allPaths,cachePath):
    if start == end:
        newTempArr = []
        newTempArr.extend(path)
        allPaths.append(newTempArr)
        return True
    rFlag, dFlag = False,False
    if checkValidCell(mat, start,"right"):
        right =(start[0],start[1]+1)
        #print(start," --> ", right)
        path.append(right)
        if right in cachePath:
            rFlag = cachePath[right]
        else:
            rFlag = checkPath(mat,right, end,path,allPaths,cachePath)
            cachePath[right] = rFlag
        path.pop()
    if checkValidCell(mat, start, "down"):
        down = (start[0]+1,start[1])
        #print(start," --> ", down)
        path.append(down)
        if down in cachePath:
            dFlag = cachePath[down]
        else:
            dFlag = checkPath(mat,down, end,path,allPaths,cachePath)
            cachePath[down] = dFlag
        path.pop()
    return dFlag or rFlag

def checkValidCell(mat,start,dir):
    if dir == "right":
        #print(start)
        newCell = (start[0],start[1]+1)
        if newCell[1] < len(mat[0]) and mat[newCell[0]][newCell[1]] != 1:
            return True
        else:
            return False
    else:
        newCell = (start[0]+1,start[1])
        #print(newCell)
        if newCell[0] < len(mat) and mat[newCell[0]][newCell[1]] != 1:
            return True
        else:
            return False


mat = [[0,0,0,1],[1,0,1,0],[0,0,0,1],[1,0,0,1]]
mat1 = [[0,0,0,1],[1,0,1,0],[0,0,0,1],[1,0,0,0]]
print(findPathExist(mat))

def getPath(mat):
    if mat == None or not len(mat):
        return False
    path = []
    allPaths = []
    cachePath = {}
    if getPathRecur(mat, len(mat)-1, len(mat[0])-1,path,cachePath):
        return True
    return False

def getPathRecur(mat, row, col,path,cachePath):
    flgSuccess = False
    if row < 0 or col < 0 or mat[row][col]:
        return False
    if (row,col) in cachePath:
        return cachePath[(row,col)]
    isStart = True if row == 0 and col == 0 else False
    if isStart or getPathRecur(mat, row-1, col,path,cachePath) or getPathRecur(mat, row, col-1,path,cachePath):
        path.append((row,col))
        flgSuccess = True
    cachePath[(row,col)] = flgSuccess
    return flgSuccess

print(getPath(mat))