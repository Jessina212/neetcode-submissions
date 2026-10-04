# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        n1 = 1
        n2 = 1
        if root == None:
            return 0
        if root.left != None:
            n1 = 1+self.maxDepth(root.left)
        if root.right != None:
            n2 = 1+ self.maxDepth(root.right)
        
        return max(n1, n2)