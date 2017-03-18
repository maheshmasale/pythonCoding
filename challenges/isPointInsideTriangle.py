def isPointInsideTriangle(x1,y1,x2,y2,x3,y3,px,py):
    slp12 = float((y1-y2)/(x1-x2)) if x1!= x2 else 0
    slp13 = float((y1-y3)/(x1-x3)) if x1!= x3 else 0
    slp32 = float((y3-y2)/(x3-x2)) if x3!= x2 else 0

    yInter12 = y1-slp12*x1
    yInter13 = y3-slp13*x3
    yInter32 = y2-slp32*x2
    #print(yInter12,yInter32,yInter13)
    print(slp12,slp13,slp32)
    if slp12 == slp13 or slp13 == slp32:
        print('Same line')
        return 0
    splP1 = float((y1-py)/(x1-px)) if x1 != px else 0
    splP2 = float((py-y2)/(px-x2)) if px != x2 else 0
    splP3 = float((py-y3)/(px-x3)) if px != x3 else 0
    ''' #not required
    yInterP1 = py - splP1 * px
    yInterP2 = py - splP2 * px
    yInterP3 = py - splP3 * px
    print(yInterP1, yInterP2, yInterP3)
    '''
    print(splP1, splP2, splP3)
    if isBetween(splP1,slp12,slp13) and isBetween(splP2,slp12,slp32) and isBetween(splP3,slp32,slp13):
        return True
    else:
        return False

def isBetween(x,y,z):
    if y>x>z or y<x<z:
        return True
    return False


def isPointInsideTriangle_area(x1,y1,x2,y2,x3,y3,px,py):
    triangleArea1 = getTriangleArea(x1,y1,x2,y2,x3,y3)
    if triangleArea1 == 0:
        print("Not a triangle")
        return 0
    triangleArea12  = getTriangleArea(x1,y1,x2,y2,px,py)
    triangleArea13  = getTriangleArea(x1,y1,px,py,x3,y3)
    triangleArea32  = getTriangleArea(px,py,x2,y2,x3,y3)
    print(triangleArea1)
    print(triangleArea12)
    print(triangleArea13)
    print(triangleArea32)


def getTriangleArea(x1,y1,x2,y2,x3,y3):
    return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2

#print(isPointInsideTriangle(3,1,7,1,5,5,1,1))
#print(isPointInsideTriangle(0,0,2,0,4,0,4,0))
#print(isPointInsideTriangle(3,1,7,1,5,5,0,0))
print(isPointInsideTriangle(3,1,7,1,5,5,1,0))
print(isPointInsideTriangle_area(3,1,7,1,5,5,6,3))
#isPointInsideTriangle(1,1,2,2,3,3,2,2)