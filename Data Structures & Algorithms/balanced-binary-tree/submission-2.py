# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root == None:
                return 0

            return max(height(root.left),  height(root.right)) + 1
        
        if root == None:
            return True
        
        if abs(height(root.left) - height(root.right)) < 2:
            flag1 = self.isBalanced(root.left)
            flag2 = self.isBalanced(root.right)
            return flag1 and flag2
        else:
            return False