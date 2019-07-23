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

    def height(self):
            return self.__height(self.root)
            
    def getHeight(self,root):
        #Write your code here
        if not root:
            return -1
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        return 1+(left_height>right_height and [left_height] or [right_height])[0]


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       