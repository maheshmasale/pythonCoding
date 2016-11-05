#https://www.hackerrank.com/challenges/matrix-rotation-algo
#Array limit --> thus i will be using numpy array

'''
import numpy as np

m,n,r = 4,2,1
#a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
a = [['a','b'],['c','d'],['e','f'],['g','h']]

tempA = np.array(a)

if m == 1 or n == 1:
    print(a)
else:
    for i in range(r):
        #Validate matrix for rotation
            #m or n >1
        #IF valid then rotate
        layers = min(m,n)//2
        for l in range(layers):
            temp = tempA[l,l]
            #copying the top row
            tempA[l, l:n - l - 1] = tempA[l,l + 1:n - l]

            #Copying right column
            tempA[l:m-l-1,n - l-1] = tempA[l+1:m-l,n - l-1]

            #copying the bottom row
            tempA[m-l-1,l + 1:n-l] = tempA[m-l-1,l:n-l-1]

            # Copying left column
            tempA[l + 1:m - l,l] = tempA[l:m - l - 1,l]

            tempA[l+1,l] = temp
    print(a)
    print(" ")
    print(tempA)

'''

m,n,r = 3,4,55
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#a = [['a','b'],['c','d'],['e','f'],['g','h']]

layer = max(m,n)//2
for l in range(layer):
    lengthArr = 2*(m+n-2-4*l)
    if lengthArr != 0:
        r_ = r % lengthArr
        arr = []
        getDataPointFromMatrix(a,)
    else:
        #single dim array
        print(" ")