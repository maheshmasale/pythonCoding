class Solution(object):
    def getPermutation(self, globalArr, k, n, start, prefixArr):
        if k == 1:
            if n > start and n<10:
                prefixArr.append(n)
                globalArr.append(prefixArr)
            else:
                return
        else:
            for i in range(start, 10):
                tempFix = []
                tempFix.extend(prefixArr)
                tempFix.append(i)
                self.getPermutation(globalArr, k - 1, n - i, i + 1, tempFix)

    def combinationSum3(self, k, n):
        globalArr = []
        prefixArr = []
        self.getPermutation(globalArr, k, n, 1, prefixArr)
        return globalArr


g = Solution()
arr = g.combinationSum3(3,9)
print(arr)