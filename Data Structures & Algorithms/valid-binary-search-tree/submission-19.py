# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def less(self, node: Optional[TreeNode], root: Optional[TreeNode]) -> bool:  
            if not root:
                return True
            if not node:
                return True
            elif node and node.val < root.val:
                return less(self, node.left, root) and less(self, node.right, root)
            else:
                return False
        def greater(self, node: Optional[TreeNode], root: Optional[TreeNode]) -> bool:  
            if not root:
                return True
            if not node:
                return True
            elif node and node.val > root.val:
                return greater(self, node.left, root) and greater(self, node.right, root)
            else:
                return False
        if not root:
            return True
        if not root.left and not root.right:
            return True
        elif not root.left and greater(self, root.right, root):
                return self.isValidBST(root.right)
        elif not root.right and less(self, root.left, root):
                return self.isValidBST(root.left)
        elif root.left and root.right and less(self, root.left, root) and greater(self, root.right, root):
                return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False