# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, currmax):
            if not node: return 0
            if node.val >= currmax:
                self.res += 1
            currmax = max(currmax, node.val)
            dfs(node.left, currmax)
            dfs(node.right, currmax)
            
        dfs(root, root.val)
        return self.res