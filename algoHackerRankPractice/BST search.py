import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def isPresent(self, root,val):
        # Write your code here
        if root.data == None:
            return 0
        elif root.data == val:
            return 1
        elif root.data > val:
            return isPresent(root.left,val)
        else:
            return isPresent(root.right, val)
        return 0

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
