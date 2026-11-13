# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True

        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            if p and q and p.val == q.val:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
            else:
                return False
        return True