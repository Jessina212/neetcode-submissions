# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if root.left == None and root.right == None:
        #     return True
        # elif root.left == None and root.right.val > root.val:
        #     return self.isValidBST(root.right)
        # elif root.right == None and root.left.val < root.val:
        #     return self.isValidBST(root.left)
        # else:
        #     if root.left.val < root.val and root.right.val > root.val:
        #         flag1 = self.isValidBST(root.left)
        #         flag2 = self.isValidBST(root.right)
        #         return (flag1 and flag2)
        # # return False

        # class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, low, high):
            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            return validate(node.left, low, node.val) and \
                   validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))