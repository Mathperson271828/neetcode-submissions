# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = []
        queue.append(root)

        while (queue):
            curr = []
            new = []
            while (queue):
                node = queue.pop(0)
                if node:
                    curr.append(node)
                    new.append(node.val)
            if new:
                ans.append(new)

            for s in curr:
                if s:
                    if s.left:
                        queue.append(s.left)
                    if s.right:
                        queue.append(s.right)

        return ans