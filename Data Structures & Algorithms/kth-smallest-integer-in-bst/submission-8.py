# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def createDeque(self, root: Optional[TreeNode]) -> deque():
            if not root:
                return
            else:
                d = deque()
                if root.left:
                    d.extend(createDeque(self, root.left))
                d.append(root.val)
                if root.right:
                    d.extend(createDeque(self, root.right))
                return d
            
            
        ans = createDeque(self, root)

        for i, val in enumerate(ans):
            if (i+1 == k):
                return val