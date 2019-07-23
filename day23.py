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

    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            res[level].append(root.data)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)

    def levelOrder(self,root):
        res=[]
        self.preorder(root, 0, res)
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j],end=" ")
        
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
