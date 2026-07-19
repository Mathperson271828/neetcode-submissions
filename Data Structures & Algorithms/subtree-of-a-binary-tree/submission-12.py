# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            elif p and not q:
                return False
            elif not p and q:
                return False
            if (p.val == q.val):
                return isSameTree(self, p.left, q.left) and isSameTree(self, p.right, q.right)
            else:
                return False
        
        if not root:
            return False
        if (isSameTree(self, root, subRoot)):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)