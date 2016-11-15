class binaryFunctions(object):

    def getBit(self, num,offset):
        #offset starts from left and from 0 onwards
        return int((num & (1 << offset)) != 0)

    def setBit(self,num,offset ):
        return num | (1 << offset)

    def clearBit(self, num, offset):
        offsetZero = ~ (1 << offset)
        return num & offsetZero

    def clearBitSignificantToOffset(self, num, offset):
        offsetZero = (1 << offset) - 1
        return num & offsetZero

    def clearBitOffsetToZero(self,num, offset):
        offsetZero = ~((1 << (offset+1)) - 1)
        return num & offsetZero

    def updateBitIthPosition(self,num,offset,boolVal):
        val = int(boolVal) << offset
        offsetZero = ~ (1 << offset)
        return (num & offsetZero) | val

b = binaryFunctions()
print(b.getBit(65,0))
print(b.setBit(4,0))
print(b.clearBit(4,2))

print(b.clearBitSignificantToOffset(7,2))
print(b.clearBitOffsetToZero(15,1))
print(b.updateBitIthPosition(4,1, True))
