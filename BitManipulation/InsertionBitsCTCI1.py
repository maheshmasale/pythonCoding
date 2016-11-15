class binaryUpdate(object):
    def updateBits(self,n,m,j,i):
        #j-i >= len(m)
        # len(m) <= len(n)

        all1s = ~ 0
        left = all1s << (j+1)
        #print(bin(left))
        right = ((1 << i) -1)
        mask = left|right
        return (n & mask) | (m << i)


b = binaryUpdate()
print(b.updateBits(17,2,2,1))
